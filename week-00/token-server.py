from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import os
import time
from livekit import api #Library for managing rooms, participants and tracks
from dotenv import load_dotenv

class TokenRequest(BaseModel):
    room_name: Optional[str] = None
    participant_identity: Optional[str] = None
    participant_name: Optional[str] = None
    participant_metadata: Optional[str] = None
    participant_attributes: Optional[Dict[str, str]] = None
    room_config: Optional[dict] = None

load_dotenv()

app = FastAPI()

@app.post("/api/token", status_code=201)
async def get_token(request:TokenRequest):
    try:
        # App level authentication like session token or JWT or something or api key 
        # Likekit guidance:
            # TODO: Add your authentication here
            # from fastapi import Depends, Header
            # async def verify_token(authorization: str = Header(...)):
            #     # Verify JWT or session token
            #     pass
            # Then add: token_data: dict = Depends(verify_token)
        # Vairbales de entorno 
        api_key = os.getenv("LIVEKIT_API_KEY")
        api_secret = os.getenv("LIVEKIT_API_SECRET")
        server_url = os.getenv("LIVEKIT_URL")
        print(api_key)
        if not all([api_key,api_secret,server_url]):
            raise HTTPException(
                status_code=500,
                detail='Server configuration error'
            )

        room_name = request.room_name or f'room-{int(time.time())}'
        participant_identity = request.participant_identity or f'participant-{int(time.time())}'
        participant_name = request.participant_name or 'User'

        token = api.AccessToken(api_key=api_key,api_secret=api_secret) \
            .with_identity(participant_identity) \
            .with_name(participant_name) \
            .with_grants(api.VideoGrants(
                room_join=True,
                room=room_name,
                can_publish=True,
                can_subscribe=True,
            ))
        
        if request.participant_metadata:
            token = token.with_metadata(request.participant_metadata)
        if request.participant_attributes:
            token = token.with_attributes(request.participant_attributes)
        if request.room_config:
            token = token.with_room_config(request.room_config) # type: ignore
        
        participant_token = token.to_jwt()

        return {
            'server_url':server_url,
            'participant_token':participant_token
        }
    
    except Exception as e:
        print(f'Token genertion error: {e}')
        raise HTTPException(
            status_code=500,
            detail='Failed to generate the token'
        )