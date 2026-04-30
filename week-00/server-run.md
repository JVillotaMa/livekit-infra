So, for running the livekit server in my machine using docker I have pulled an image from the docker registry livekit/livekit-server.
learned a lot today about docker 

Faltaban keys y livekit tiene una herramienta para generarlas
Crear cambiar config y volver a ejecutar

Even when the port of the confifg is 7880, that does not mean that the gate is open, that just means that is the port where action ocurr.



docker run -v $PWD/livekit.yaml:/livekit.yaml -p 7882:7880 livekit/livekit-server:v1.11.0 --config /livekit.yaml
