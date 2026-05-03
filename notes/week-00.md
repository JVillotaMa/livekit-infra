Livekit is a framework (abstracts complexity) that handles all things needed (transport, communication, build) for deploying agents and being able to handle conversation fluently with users.

Agents are workers that joins to rooms on livekit server that optimizes all the infra needed for quick and low latency communication.

For the web it is used the WedbRTC protocol, unlike HTTP that is designed for request-response acitons, it is optimized for streaming media (video and audio) in real time. WebRTC can handle bad connection alone, it is a hard protocol to work with but livekit abstracts that complexity for us.

## Just for calls?
Livekit is not just a framework for calling, it is a framework for communication and networks, I can handle different meetings, or communications with humnas and introduce ai in the loop, I can build more than just calls it is a form of creating network projects: SUPER EXCITING. I can do video conferncing just for humans I can build healthcare for just having that flow of data in my loop. Handle connection with robots. INCREDIBLE. Livekits just provides the abstraction and the foundation for realtime projects using both humans and ai agents.

## How livekit works?
Livekit architecture is supported by various components that work together:

### 1. Livekit server:
Is an opensource webRTC SFU ( selective forward unit ) that handles the media streaming and the .

#### SFU
Is a communication architecture with a server at the middle of the users that handles all the heacy lifting on the multiuser communication. It handles connectivity,NAT traversal is done by clients using STUN/TURN servers, not by the SFU directly., routing adaptative degradation. 
The difference with the mesh is that with the mesh one user had to encode and send the medio to all the users by itself, with SFU, the user just sends it to the server and it handles all the media and communication with the other users. This lowers the CPU usage (audio encoding) and bandwith by a lot.

The selective part: the sfu can select to wich user prioritize based on network conditions or if it is the active user.

### 2. Livekit agents framework
This is the framework wich can create agents choosing LLM TTS and STT with full modulatity, is high level. Agents can join rooms track media receive things. Just like another human. (CAN I HAVE TWO AGENTS MAKING A JOB INTERVIEW FOR EXAMPLE!)

### 3. SDKs and clients

This is the library wich is able to create rooms join to them and make users join to the room. Suscribe or unsuscribe to roooms Same sdk for both humans and agents.

─────────────┬──────────────┬───────────────────────────┬──────────┐
  │   Acción    │    Quién     │         Qué hace          │ Direcció │
  ├─────────────┼──────────────┼───────────────────────────┼──────────┤
  │ Publish     │ Participante │ Empieza a emitir su track │ Outbound │
  │             │  A           │  (cámara/micro) al SFU    │          │
  ├─────────────┼──────────────┼───────────────────────────┼──────────┤
  │ Unpublish   │ Participante │ Deja de emitir el track.  │ Outbound │
  │             │  A           │ Desaparece para todos.    │          │
  ├─────────────┼──────────────┼───────────────────────────┼──────────┤
  │             │ Participante │ Sigue publicado pero no   │          │
  │ Mute        │  A           │ envía datos (placeholder  │ Outbound │
  │             │              │ negro/silencio)           │          │
  ├─────────────┼──────────────┼───────────────────────────┼──────────┤
  │ Subscribe   │ Participante │ Recibe el track de A      │ Inbound  │
  │             │  B           │                           │          │
  ├─────────────┼──────────────┼───────────────────────────┼──────────┤
  │             │ Participante │ Deja de recibir el track  │          │
  │ Unsubscribe │  B           │ de A (A sigue publicando  │ Inbound  │
  │             │              │ para los demás)           │          │
  └─────────────┴──────────────┴───────────────────────────┴──────────┘


### 4. Integration services
Livekit integrates different communication methods like SIP or Egreess etc.


# Core concepts

Livekit being a realtime platform, is built around rooms, participants and tracks. Those are virtual spaces where participants (users and agents) connect and share media across the platform (or embeded) that we want.

## Rooms, participants and tracks
These three components inside the sdk are the ones wich have all the Livekit applications, most fundamental ones.

- **Room**: virtual space where all the participants are and where the communication happens.
    - Capabilites: delete create and list
- **Participants**: are the users, agents and services that joins a room.
    - Capabilituies: list remove and mute
- **Tracks**: are the media streaming where participants can suscribe and publish on.
    - Capabilities: videocamera, microphone and screen share tracks (publish and suscribe)


# Arquitectura 
Livekit is an individual server IS NOT A LIBRARY THAT I USE, is a server by itself running in a docker that manages rooms participants and all the connections.

Above that server, I can manage that server using my server code using sdk server with go so I can create roomns, manage participants and manage tracks (not for this week 0), we are delegating  all that runtime operations to the SFU that runs on our server.

![alt text](image.png)



# Docker

Why to use docker, don't have to complain about OS the machine. Machine is solated and have ALL it is need.

## Contanier

Is an isolated environment. Is like a mobile aplication. Apps are not affected by each other.

docker run <container> -> run the container.
docker ps               -> see the containers runnign
docker stop <contanier_id> -> stop a container

## Images
Is where all needed for running the applicaction, are standarized packages where lives all the code of your app.
Standareized packages where all the necessary (binaries, codes, files) things live for running your application.

You pull docker images and you can run it directly into a container.

1. Is inmmutable
2. Is made of layers -> create layers (you can build on top of that without managing those dependecnies)


IMAGES > CONTAINER

docker search docker/welcome-to-docker -> searches in the docker marketplace an image called welcome-to-docker
docker pull docker/welcome-to-docker -> pull an image 
docker image history docker/welcome-to-docker -> layers of an image


# MUST KNOWN COMMAND TO DOCKER
-v: <&PWD/<file.yaml>>:<path_in_docker>mount files into the image, being able to use the yaml on the image and llinkid it. 
-p: port redirection  <my-machine-port>:<docker-port>
--config <path_in_docker>: normally the route to the config file

SIntaxis is before the image
docker run -v <> -p<> <image> --config 

### Ports
Even when the configuration in the yaml has a port configured BUT that port is not for opening the gate to the world, that port is just the "where is the play"

# What i have learned about opensource and configuration

normally, in opensource project we must go the source to understand all the code and configuration needed to run the application.

Before knowing that I was unable to run the livekit-server image because i had not a guide to use it. Now, I understand it and i can.

Based on history, OOSS projects are fail by defualt so yo can't run the application without handling the configuration. THis is done like that to ensure correct configuration and security enhancement.



# Tokens & Grants

For making the users able to connect with the SDK to the server it has to be passed an **access token** with the request.
The **access token** encodes the grants, identity,permission and other parameter of the user. The **access tokens are JWT-based and signed with the API secret (livekit)** to prevent false requests.
Those tokens have time expiracy for the first connection, not subsequent reconnects. A request for connection with an expired token gets rejected by livekit server.

## Token structure
The access token are JWT's that contains JWT base informaion and livekit specific info like identity, room, expire time and **grants**

For exmaple the decoded bod of an access token:
{
  "exp": 1621657263,
  "iss": "APIMmxiL8rquKztZEoZJV9Fb",
  "sub": "myidentity",
  "nbf": 1619065263,
  "video": {
    "room": "myroom",
    "roomJoin": true
  },
  "metadata": ""
}
In here you can see video grants, the identitu,, iss is the API token, exp is the expire time and video is video grants including room permision.

## Token refresh

Livekit serves automatically refresh tokens to the participants to reconnnect if they want to. THose refresh tokens have 10 min expiracy time.
Whenever the user identity is changed or their permissions, likevit issue refresh the token automatically so the other token can't be used again.

When th eparticipant's permission are changed or is deleted from the room, the token used to access the room gets revoked so it can't be used.

## GRANTS AND PERMISSION
The tokens are the way to handle permissions  to the participants on the room, you can see more in https://docs.livekit.io/frontends/reference/tokens-grants/ 

## Generating the token

TO use the sdk in the client we must generate a token that uses api secret so it must be generated in our backend. TO simplify all the permissions, refreshing etc that livkeit uses as discused early, we can user ToeknSource abstraction. That abstraction can integratie with Session objetc to directly connect to a room.

TokenSource have different types for token generation

Sandbox -> used for Livekit Cloud (not our use case)
Endpoint -> provide a token standarized endpoint in our backend and livekit maanges all the token lifecycle.
Custom -> Provide our async custom token manager and generator
Literal-> Directly provide our tokens.

Our use case we will use endpoint type to handle token generation and usability.

### Authentication flow

1. Client asks for a token to our server
2. Server serves the token (with thte permissions that we want) (using the endpoint type)
3. Client connects to livekit using it using Session, that happens automaticaaly TOkenSOurve fetched the token and session habndles the connection. 

### CRITICAL
In the token generation de the api and secret keys are not validated with the livekit server, they are just served.

# Connection between api and front

Fastapi was waiting a json request but I was sending a js object so i constantly received a 422 error, i have to serialize (transform de js object into JSON to do it.)

It is done by JSON.stringify


I have discoverd in the config.yaml of livekit that the api key and secret were pairs apiKey:secretKey


# Media and track
the client sdk can enable microphone and camera permissions using

room.localParticipant.setCameraEnabled(true)
room.localParticipant.setMicrophoneEnabled(true)

This what is doing is
1. Connection to the device via de browser
2. Creates the track locally
3. Publishses to the SFU

What we need now is to get that data from the published data in the SFU and insert it into de DOM.

## How to debug if audio is publishing and receibing?
In console in publisher:

*room.localParticipant.trackPublications*

That command gives you the tracks that are being sent to the SFU.

In console in suscriber:

*console.log('Remote participants:', Array.from(room.remoteParticipants.values()).map(p => ({
      identity: p.identity,                                                                                                                                                                   
      tracks: p.trackPublications.size
  })));*

To see which tracks i am receiving from the other participants.

and in suscriber console as well:
*const remoto = Array.from(room.remoteParticipants.values())[0];                                                                                                                             
  remoto.trackPublications.forEach(pub => {                                                                                                                                                   
      console.log(pub.kind, '| subscribed:', pub.isSubscribed, '| attached elements:', pub.track?.attachedElements?.length || 0);
  });    *

So we can know if the tracks that we are receiving are being attached to a component and being seen in the DOM. IF they are not being rendered in the DOM the client cannot listen to that.

## Suscribring to a track

By default, when a participant joins a room, there is autoSuscribe enable by default so the client is receiving all the tracks and they are ready for render it.

### 1. Suscribe to the track data from the server

Livekit has two constructs to track media:
- TrackPublication: Media metadata, all the listeners have access to it even when there are no suscribers of the raw data of the track
- Track: raw media stream

SO the way of suscribing to that is a Javascript callback that suscribes to both of the constructs.

```js
room.on(RoomEvent.TrackSuscribed, handleTrackSuscribed)
function handleTrackSuscribed(
  track: RemoteTrack,
  publication: RemoteTrackPublication,
  participant: RemoteParticipant,
){
  /* DO things with the track*/
  // Attach track to a new HTMLVIdeoElement or HTMLAUdioElement
  const element = track.attach()
  parentElement.appendChild(element)
  //Or attach ot existing element
  // track.attach(element)
}
```


# Debgugginh

to verify connection repeteadly put 

```js
console.log({                                                                                                                                                                               
      state: room.state,                                                                                                                                                                    
      localTracks: room.localParticipant.trackPublications.size,                                                                                                                              
      remoteParticipants: room.remoteParticipants.size,                                                                                                                                       
      canPlayback: room.canPlaybackAudio                                                                                                                                                      
  });     
  ```


# ERROR CRITICO EDUCATIVO

I have encountered this error
```
livekit-client.umd.js:1 Uncaught (in promise) ConnectionError: could not establish pc connection
    at livekit-client.umd.js:1:207341
```

that meant that the connection via TCP to the SFU was successful, but when the participant tried to connect via UDP to the SFU to track media and tried all the ICE candidates, it coudn't connect.
That is because the browser has not been able to solve the ip and there is no ports for UDP in the docker that are ready for connections.


  What happened was that our signaling layer was funcitonign (TCP working and connection done)

# ICE failed WebRTC
When a client connects to a SFU using webrtc, the SFU serves candidates. The client using webRTC tries all the candidates and the first connecting is the one that is used by the client. WebRTC negotiates

### Principal content:
We use two different channgels of data signaling and media. Signaling is done via TCP and media via UDP and one of them can be broken. The problem is usuarlly routers, NAT and firewalls. #1 production bug with WebRTC

# ICE
ICE is the negotiation process peers to find a actionable route.
1. Every peer (our browser and SFU) share candidates list. A candidate is a tuple (IP, puerto, protocolo, tipo). Ejemplo:                                                   
    - (192.168.1.50, 50012, UDP, host) ← una IP local del SFU
    - (188.86.113.76, 50012, UDP, srflx) ← su IP pública vía STUN                                                                                                                        - (10.0.0.5, 7881, TCP, host) ← fallback TCP                                                     

2. The other peer test connections and the first connecting wings
3. If all fails -> ICE failed -> could not establish pc connection.


So the fix is telling livekit in the config to show private ips so the SFU shows local candidates to the browser and the browser can resolve those. Furthermore, we need to handle new connections using docker bridges


# NAT

NAT is a way of using just one public IP for multiple clients.

How it works: i want to connect to 8.8.8.8
My browser/pc: private 127.0.0.1
GOes to my router: private 192.168.1.1 inside, but outside 188.86.113.76 to internet.

So if someone from Ukrains wants to connect with me it can't because is private.

Solo tu router tiene una IP pública, y la comparte con todos los dispositivos de tu casa.                                                                                                   
                  
  Salida: connection outbound (lo que SÍ funciona)                                                                                                                                            
                  
  Tu portátil quiere abrir google.com:                                                                                                                                                        
                  
  1. Portátil envía paquete: desde 192.168.1.50:54321 hacia 142.250.184.78:443 (Google).                                                                                                      
  2. Paquete sale por router. Router lo intercepta y lo reescribe (esto es la "translación"):
    - Cambia el origen: ahora es desde 188.86.113.76:54321 hacia 142.250.184.78:443.                                                                                                          
    - Anota en una tabla: "puerto externo 54321 ↔ portátil 192.168.1.50:54321".                                                                                                               
  3. Google recibe el paquete, ve que viene de 188.86.113.76, responde a esa IP.                                                                                                              
  4. La respuesta llega al router: desde 142.250.184.78:443 hacia 188.86.113.76:54321.                                                                                                        
  5. Router consulta su tabla, ve "54321 era del portátil", reescribe el destino y reenvía:                                                                                                   
    - desde 142.250.184.78:443 hacia 192.168.1.50:54321.                                                                                                                                      
  6. Tu portátil recibe la respuesta. Cree que habló directamente con Google.                                                                                                                 
                                                                                                                                                                                              
  Magia: los 50 dispositivos de tu casa pueden navegar simultáneamente con una sola IP pública. Cada uno usa puertos distintos en la tabla del router.                                        
                                                                                                                                                                                              
  El problema de NAT: tráfico inbound                                                                                                                                                         
                  
  Imagina que alguien en internet quiere conectarse a tu portátil sin que tú hayas iniciado la conversación. ¿A qué dirección envía el paquete?                                               
                  
  - 192.168.1.50 → no se enruta en internet, paquete se pierde.                                                                                                                               
  - 188.86.113.76 → llega a tu router, pero el router no tiene ni idea de a qué dispositivo interno reenviar. Su tabla solo tiene entradas para conexiones iniciadas desde dentro.
                                                                                                                                                                                              
  Resultado: los dispositivos detrás de NAT son inalcanzables desde fuera por defecto. Solo pueden iniciar conexiones, no recibirlas.                                                         
                                                                                                                                                                                              
  Esto es enorme para internet:                                                                                                                                                               
  - ✅ Bueno para clientes (laptop, móvil) — añade una capa de "firewall" gratis.
  - ❌ Malo para servidores — necesitan port forwarding explícito en el router para recibir tráfico.                                                                                          
  - ❌ Catastrófico para P2P / WebRTC — dos peers detrás de NAT no pueden hablarse directamente.   


  Por qué tu LiveKit fallaba — NAT hairpinning                                                                                                                                                       
  Tu caso fue una variante específica llamada NAT hairpinning (o NAT loopback):                                                                                                               
                  
  1. Tu LiveKit en Docker descubrió vía STUN su IP pública: 188.86.113.76.                                                                                                                    
  2. Anunció a los clientes: "para enviarme media UDP, usa 188.86.113.76:50012".
  3. Tu navegador en el mismo localhost intentó conectar a 188.86.113.76:50012.                                                                                                               
  4. El paquete sale de tu navegador → router → ¡pero el destino es tu propio router!                                                                                                         
  5. El router, dependiendo de su firmware, a veces no soporta hairpinning (volver a entrar por su propia IP pública). El paquete se pierde.