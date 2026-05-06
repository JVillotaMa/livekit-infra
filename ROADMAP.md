# Roadmap Infra / DevOps — 4 meses

**Autor:** Jaime Villota
**Inicio:** 2026-04-28
**Fin objetivo:** 2026-08-30 (~17 semanas, incluye Semana 8 de telefonía SIP)
**Carga:** 2h/día L-V + 2-3h sábado ≈ 12-13h/semana
**Vehículo:** proyecto LiveKit self-hosted (calling infra)
**Conversacion**: claude --resume d2e4d66f-db15-4e6b-aa7d-3062a32478e2

---

## 1. Objetivos

Al terminar los 4 meses tienes que poder:

1. Levantar infraestructura de producción real en AWS desde cero con Terraform.
2. Operar un servicio stateful en tiempo real (LiveKit) con observabilidad y alertas decentes.
3. Desplegar y mantener un cluster Kubernetes pequeño con CI/CD automatizado.
4. Defender en una entrevista decisiones de arquitectura, costes, trade-offs.
5. Tener proyecto público en GitHub + 2 posts técnicos publicados.

Output esperado: perfil **dev senior con infra real** o **DevOps junior empleable**, top 20% del mercado español por escasez del combo.

---

## 2. Filosofía

- **LiveKit es la columna vertebral.** Cada concepto que aprendes lo aplicas al proyecto en la misma semana. Nada de teoría sin destino.
- **Construir > leer.** Si una semana no produce código/infra, esa semana ha fallado.
- **Sin agentes de IA generando código durante el aprendizaje.** Reglas en sección 2.1.
- **Time-boxed.** Si una semana se atasca, avanzas igual y vuelves al gap luego. La perfección mata el roadmap.
- **Notas semanales.** Markdown, en este mismo repo. Vas a olvidar el 70%, las notas son tu segunda memoria.
- **Público desde día 1.** Repo en GitHub público, commits diarios aunque sean WIP.
- **Aplicar a curros desde semana 10**, no semana 16. Las primeras entrevistas son entrenamiento.

### 2.1 Política de uso de IA durante estos 4 meses

**Regla central:** durante el aprendizaje, **la IA no escribe código por ti**. Lo escribes tú, leyendo docs y source code. Sin excepciones para "ahorrar tiempo" — ese atajo destruye la fijación de conceptos.

**Qué SÍ está permitido (uso "diccionario"):**

- Preguntar a un LLM **qué significa** un concepto que ya leíste y no entiendes.
- Usar IA para **traducir errores** crípticos a explicación legible.
- Pedir **comparativas conceptuales** (ej: "diferencia entre StatefulSet y Deployment").
- Aclaraciones sobre **sintaxis del lenguaje** ya leída en docs.

**Qué NO está permitido:**

- Que la IA **escriba un Dockerfile, módulo Terraform, manifest de K8s, etc.** que tú vas a usar tal cual.
- Pegar un error largo y aceptar la solución sin entender la causa raíz.
- Autocompletado tipo Copilot/Cursor en este repo. Desactívalo.
- Generar boilerplate "porque es repetitivo". Especialmente Terraform e YAML — ahí está el aprendizaje.
- Agentes autónomos (Claude Code, Cursor agent, Aider) ejecutando tareas en el repo.

**Test rápido:** si después de leer la respuesta de la IA pudieras explicar el código a otra persona línea a línea y reescribirlo de cero sin volver a mirarla → uso correcto. Si no → estás haciendo trampa contigo mismo.

**Cuándo levantar la veda:** cuando empieces a aplicar a curros (semana 10+), puedes usar IA para acelerar tareas que ya dominas (Sonalyx, otros side projects). El repo de formación sigue siendo zona libre de IA hasta el final.

**Por qué esta regla es estricta:**

- WebRTC, networking, K8s, Terraform tienen modelos mentales que solo se forman peleándote tú con ellos.
- Los LLMs alucinan en infra (flags obsoletos, APIs inexistentes, versiones mezcladas). Si no lo detectas, depuras horas. Si lo detectas, es porque ya sabías — entonces para qué preguntaste.
- Tu ventaja competitiva post-2025 no es "saber prompt engineering". Es **saber lo que la IA no sabe**. Eso solo se construye yendo a primer principios.

---

## 3. Estudio vs Práctica

Las 2h diarias entre semana se reparten típicamente **30 min estudio + 90 min práctica**.

### Estudio (~30 min)
Leer y entender el concepto del día. Output mental, no código.

- 1 capítulo de libro / sección de docs / vídeo de curso.
- Notas breves en Markdown (qué es, para qué, dónde encaja).
- Si aparece un comando o snippet: lo copias en notas pero **no lo ejecutas todavía**.
- Si te aburres leyendo: la lectura no está aterrizada en un problema concreto. Salta a práctica y vuelve.

### Práctica (~90 min)
Manos en el teclado. Código, terminal, infra real.

- Aplicar lo leído al proyecto LiveKit.
- Escribir Dockerfiles, Terraform, manifests, configs.
- Romper cosas a propósito y arreglarlas.
- Commit + push al repo al terminar la sesión, aunque sea WIP.

**Regla:** ningún día es 100% lectura. Si solo tienes 1h, prioriza práctica.

---

## 4. El sábado — qué es y qué no es

**No es un examen.** No es revalidar lo de la semana.

**Sí es:** la sesión larga donde **terminas el deliverable**. Durante L-V vas construyendo en piezas pequeñas (1.5h máximo de práctica/día no da para terminar un deliverable completo). El sábado tienes 2-3h de bloque continuo para integrar, pulir, documentar y dejarlo demoable.

**Estructura típica del sábado:**
- 30 min: revisar dónde quedó el deliverable, qué falta.
- 90-120 min: terminarlo, hacer que funcione end-to-end.
- 30 min: README de la semana (qué se hizo, comandos, screenshots, gotchas), commit final, push.

**Domingo:** descanso o 30 min de retro escrita. Cerebro necesita off para consolidar.

---

## 5. Horario semanal tipo

| Día | Bloque | Duración | Contenido |
|-----|--------|----------|-----------|
| Lunes | Estudio + práctica | 2h | Concepto nuevo de la semana + primera implementación |
| Martes | Práctica + estudio | 2h | Avance del deliverable + lectura complementaria |
| Miércoles | Práctica | 2h | Profundizar implementación |
| Jueves | Práctica | 2h | Resolver bloqueos, ajustar |
| Viernes | Práctica + retro | 1.5h + 0.5h | Última pieza + retro semanal escrita |
| Sábado | Sesión larga | 2-3h | Cerrar deliverable, README, commit final |
| Domingo | Off / retro opcional | 0-30 min | Descanso |

**Total:** 12-13h/semana × 17 semanas ≈ **210h reales** (Semana 8 SIP es algo más densa: ~14h).

**Franja horaria:** elige una (mañana 7-9, mediodía 13-15, o tarde 18-20) y mantenla. La constancia compone más que la cantidad.

---

## 6. Roadmap mes a mes

### MES 0 — Toma de contacto (solo web, sin SIP)

#### Semana 0 · LiveKit funcionando en local
**Objetivo:** tener LiveKit corriendo en tu máquina y un cliente web conectándose **antes** de empezar Semana 1. Sin esto, Docker en Semana 1 es contenedorizar en abstracto. Aquí no estudias en serio: te expones a los conceptos para que las semanas siguientes apliquen sobre algo concreto.

**Carga total:** 4-6h. Un fin de semana o dos tardes. No más.

**Deliverable concreto:**

Repo `livekit-infra` creado en GitHub público con esta estructura mínima:

```
livekit-infra/
├── README.md
└── week-00/
    ├── notes.md           # Conceptos con tus palabras
    ├── server-run.md      # Comando docker run del server + variables que usaste
    ├── token_server.py    # Script Python que genera tokens
    └── client/
        └── index.html     # Cliente web mínimo con livekit-client JS
```

Funcionando end-to-end:
1. `docker run` levanta el LiveKit server en localhost.
2. `python token_server.py` arranca un mini servidor HTTP (Flask o FastAPI) con un endpoint `/token?room=test&identity=jaime` que devuelve un JWT firmado.
3. Abres `client/index.html` en dos pestañas del navegador. Cada una pide un token al endpoint y se conecta a la misma room.
4. Ves a los dos participantes, audio y video funcionando entre ellos.

**Bloques de trabajo sugeridos:**

| Bloque | Tiempo | Qué hacer |
|--------|--------|-----------|
| 1. Conceptos | 1h | Leer "Introduction" + "Core concepts" en docs.livekit.io. Escribir `notes.md` con tus palabras: qué es SFU, Room, Participant, Track, Publication, Token. Sin copiar-pegar de la doc. |
| 2. Server local | 1h | `docker run` del server oficial (`livekit/livekit-server`) con un `livekit.yaml` mínimo. Documentar comando y config en `server-run.md`. |
| 3. Token server | 1.5h | Script Python con `livekit-api` SDK que genera access tokens. Endpoint HTTP simple. Probar con curl que devuelve un JWT. |
| 4. Cliente web | 2h | HTML + JS con `livekit-client` (vía CDN). Pide token al endpoint, conecta a la room, muestra remote participants en `<video>` tags. |

**Restricciones explícitas (importantes):**

- **Solo web a web.** Nada de SIP, nada de telefonía, nada de números. Browser ↔ Browser.
- **Solo localhost.** Sin TLS, sin dominio, sin cloud. Eso es Semana 7.
- **Sin Compose.** `docker run` plano. Compose es Semana 1.
- **Sin frameworks de cliente.** HTML estático + JS plano. React/Vue ahora es ruido.
- **El código lo escribes tú.** Copias snippets de la documentación oficial leyéndolos. **No le pides a un LLM que escriba el script ni el HTML.** Sección 2.1 ya aplica.

**Notas mínimas que tienen que estar en `notes.md`:**

Responde con tus palabras (1-3 frases cada una):
1. ¿Qué es un SFU y por qué LiveKit lo es?
2. ¿Cuál es la relación entre Room, Participant, Track y Publication?
3. ¿Qué información lleva un access token y por qué se firma server-side?
4. ¿Qué pasa cuando un cliente publica un track? ¿A qué otros participantes les llega?
5. ¿Qué puertos (TCP/UDP) usa LiveKit y para qué?

Si no puedes responder a las 5 sin abrir docs, repasa antes de pasar a Semana 1.

**Lo que NO haces aún:**

- SIP, agents, egress, ingress.
- Self-host serio con TLS, dominio, TURN propio. (Semana 7)
- Despliegue en cloud. (Semanas 3-4)
- Código en Go, ni servicios complejos. (Más adelante)
- Frontend bonito.

---

### MES 1 — Fundamentos sólidos

#### Semana 1 · Docker de verdad
- **Deliverable:** el setup de Semana 0 ahora con Dockerfile propio para el token-server (multi-stage <50MB, healthcheck, non-root) + `docker-compose.yml` que orquesta `livekit-server` + `token-server` + (opcional) `redis`. Network custom entre ellos. Cliente web servido por nginx alpine en otro contenedor. Todo levanta con `docker compose up`.
- **Estudio:** multi-stage builds, layer caching, volumes vs bind mounts, networks (bridge/host/custom), BuildKit/buildx, security básica.
- **Recurso:** *Docker Deep Dive* (Nigel Poulton) + docs oficiales "Best practices for writing Dockerfiles".

#### Semana 2 · Redes (refresh + producción)
- **Deliverable:** documento Markdown con diagrama explicando paso a paso qué pasa cuando un cliente conecta a `livekit.tudominio.com`. DNS → TCP → TLS → WebSocket → media UDP.
- **Estudio:** TCP vs UDP a fondo, DNS (records/TTL/propagación), TLS 1.3 handshake, HTTP/1.1 vs 2 vs 3 (QUIC), WebSocket, NAT/STUN/TURN/ICE.
- **Recurso:** *High Performance Browser Networking* (Grigorik, gratis en hpbn.co), capítulos 1-4.
- **Skip:** BGP, OSPF, routing protocols. No los necesitas.

#### Semana 3 · AWS fundamentos
- **Deliverable:** VPC con subnets pública/privada, EC2 con SSH, RDS Postgres, S3 privado, dominio en Route 53. Todo a mano por consola, screenshots en notas.
- **Estudio:** IAM (users/roles/policies), VPC + subnets + route tables + NAT gateway, security groups, EC2 (AMIs, key pairs), S3 (policies, versioning), Route 53.
- **Recurso:** curso de **Adrian Cantrill (SAA-C03)** — el mejor del mercado.
- **Decisión:** AWS sobre GCP por demanda en mercado español. Si Sonalyx ya está en GCP, GCP.

#### Semana 4 · Primer Terraform + LiveKit en VM
- **Deliverable:** Terraform que crea VPC + EC2 + RDS + Redis. Encima, LiveKit con docker-compose corriendo. Llamada de prueba funcional desde navegador.
- **Estudio:** sintaxis HCL, providers/resources/data sources, variables/outputs/locals, state local (luego remoto), módulos triviales.
- **Recurso:** *Terraform: Up & Running* (Yevgeniy Brikman).

---

### MES 2 — Producción light

#### Semana 5 · Terraform a fondo
- **Deliverable:** infra LiveKit como módulo Terraform reusable, state remoto en S3 + DynamoDB lock, dos environments (staging, prod) con configuraciones distintas.
- **Estudio:** módulos bien estructurados, remote state, locking, workspaces vs múltiples directorios (preferir directorios), `terraform plan` en CI básico.

#### Semana 6 · Observabilidad
- **Deliverable:** Grafana con dashboard real de LiveKit (rooms activas, participants, CPU, memoria, packet loss), logs centralizados en Loki, 3 alertas en Alertmanager.
- **Estudio:** Prometheus (scrape configs, PromQL básico), Grafana (datasources, dashboards), Loki (log aggregation), Alertmanager, métricas RED y USE.
- **Recurso:** libro *Site Reliability Engineering* (Google, gratis online), capítulos sobre SLOs y monitoring.
- **Bonus:** LiveKit expone métricas Prometheus nativas, no hay que instrumentar nada.

#### Semana 7 · TURN + TLS + Dominio real
- **Deliverable:** LiveKit accesible desde `livekit.tudominio.com` con TLS auto-renovado (Let's Encrypt), coturn propio funcionando, llamada funcional desde móvil 4G atravesando NAT.
- **Estudio:** coturn config (realm, auth, listening ports, range UDP), Let's Encrypt + cert-manager o Caddy, DNS A/AAAA, reverse proxy.
- **Recomendación:** **Caddy** sobre nginx para esto, mucho más simple para certs automáticos.

#### Semana 8 · Telefonía SIP (la que conecta el roadmap con Sonalyx)
- **Deliverable:** llamada telefónica real desde un móvil cualquiera a un número que tú controlas, que entra a una room de LiveKit donde un participante (browser o agent) puede hablar. Audio bidireccional funcional. Logs de la llamada en tu Grafana.
- **Estudio:** SIP/RTP fundamentals (signaling vs media), trunk providers (Telnyx/Twilio/Voxbeam), `livekit-sip`, dispatch rules, DID, PSTN, codecs telefónicos (Opus vs G.711).
- **Recurso:** `docs.livekit.io/sip/` + `github.com/livekit/sip` + Telnyx Developer Portal.
- **Pre-requisitos:** Semana 7 cerrada (TURN + TLS + dominio funcionando). SIP sin esa base es ejercicio de juguete.
- **Por qué AQUÍ:** acabas de montar TURN, TLS y dominio. SIP necesita exactamente eso para conectar trunks reales. Insertar SIP ahora aprovecha la base recién hecha y conecta el aprendizaje de infra con el producto real de Sonalyx.

**Plan de la semana (más densa: 2h/día + sábado largo):**

- **Día 1:** lectura de conceptos SIP/RTP/PSTN. Crear cuenta en Telnyx (o Voxbeam si prefieres provider español). Comprar 1 número (~$1-2/mes). Anotar credenciales del trunk.
- **Día 2:** añadir `livekit/sip` al `docker-compose.yml`. Configurar `sip.yaml` mínimo conectado a tu LiveKit. Verificar que arranca y se registra.
- **Día 3:** crear inbound trunk en LiveKit (vía API o `livekit-cli`). Configurar dispatch rule básico ("cualquier llamada → room `support`"). Configurar el provider para rutear al `livekit-sip`.
- **Día 4:** **primera llamada real**. Marcar tu número desde un móvil. Verificar en logs que entra. Verificar participant en la room. Conectar tu cliente web a la misma room y hablar contigo mismo.
- **Día 5:** routing dinámico — `services/sip-dispatcher/` Python que recibe webhooks de eventos SIP y decide room según número marcado.
- **Día 6:** outbound calls — configurar el trunk para originar llamadas. Test: script que te llama al móvil, contestas, entras en room.
- **Día 7:** observabilidad — métricas Prometheus de `livekit-sip` integradas en Grafana. Runbooks: "llamada conecta sin audio" (RTP/NAT), "trunk no se registra" (credenciales), "llamada se cae a 30s" (timeout NAT).

**Estructura nueva en el repo:**

```
livekit-infra/
├── services/
│   └── sip-dispatcher/         # NUEVO — webhook handler + routing
│       ├── main.py
│       └── Dockerfile
├── docker/
│   ├── docker-compose.yml      # añade servicio livekit-sip
│   └── sip.yaml                # NUEVO — config livekit-sip
├── docs/
│   ├── decisions/
│   │   └── 0XX-sip-trunk-provider.md   # NUEVO — ADR provider elegido
│   └── sip-architecture.md     # NUEVO — diagrama flujo SIP→LiveKit
├── runbooks/
│   ├── sip-call-no-audio.md    # NUEVO
│   ├── trunk-not-registered.md # NUEVO
│   └── sip-call-drops-30s.md   # NUEVO
└── scripts/
    └── test-sip-call.sh        # NUEVO
```

**Costes esperados (Telnyx, 2026):**
- Número EU: ~$1-2/mes.
- Inbound EU: $0.0035-0.0075/min.
- Outbound EU: $0.005-0.015/min.
- **Total semana de aprendizaje:** ~$5-15.

**Trampas conocidas:**
- **NAT y RTP:** la mayoría de "llamada conecta pero no oye" es UDP/NAT. `livekit-sip` puede necesitar IPs explícitas en config.
- **Codec mismatch:** provider envía Opus o G.711, ambos deben aceptarse.
- **Credenciales:** trunk password en secret manager o env var, **NUNCA committeado**.
- **Costes runaway:** un bug en outbound puede llamar 1000 veces. **Pon spending caps en el provider desde Día 1.**
- **Compliance:** grabar llamadas en EU requiere consentimiento (RGPD).

**Tools de debugging que necesitas conocer:** Wireshark + `sngrep` (te muestra el flow SIP en formato call-flow diagram, brutal cuando algo no conecta).

#### Semana 9 · Load testing + tuning
- **Deliverable:** simular 50-100 llamadas concurrentes con `livekit-cli load-test`, gráficas de Grafana mostrando dónde se rompe, ajustes de sistema (sysctl, ulimits) documentados con before/after.
- **Estudio:** load testing approaches, `htop`/`iotop`/`ss`/`tcpdump` básico, sysctl tuning para muchas conexiones UDP, vertical vs horizontal scaling.

---

### MES 3 — Escalar y automatizar

#### Semana 10 · Kubernetes fundamentos
- **Deliverable:** cluster k3s en una VPS con 2-3 servicios tontos desplegados (NGINX + app simple + Redis). **No LiveKit aún.**
- **Estudio:** Pods, ReplicaSets, Deployments, Services (ClusterIP/NodePort/LoadBalancer), ConfigMaps, Secrets, namespaces, `kubectl` con fluidez.
- **Recurso:** *Kubernetes Up & Running* (Hightower, Burns, Beda).
- **Skip por ahora:** "Kubernetes The Hard Way" (masoquismo opcional, no necesario).

#### Semana 11 · K8s producción-light
- **Deliverable:** LiveKit en K8s con Helm chart oficial, ingress configurado, persistent volumes, HPA con métricas custom.
- **Estudio:** Helm (charts/values/templates), ingress controllers (nginx-ingress o Traefik), StatefulSets para datos persistentes, resource requests/limits, HPA.
- **EMPIEZA A APLICAR A CURROS ESTA SEMANA.** No esperes a sentirte listo. Las primeras entrevistas son entrenamiento.

#### Semana 12 · CI/CD
- **Deliverable:** push a `main` → tests → build Docker → push a registry → deploy automático al cluster. PR previews opcionales.
- **Estudio:** GitHub Actions (workflows, jobs, matrix, caching), GHCR/ECR, GitOps con ArgoCD, secrets en CI vía OIDC con AWS (no más secrets hardcoded).

#### Semana 13 · Seguridad
- **Deliverable:** secrets gestionados con SOPS o External Secrets Operator, IAM auditado con mínimo privilegio, NetworkPolicies en cluster, scan de imágenes Docker en CI con Trivy.
- **Estudio:** secrets management patterns, IAM least-privilege, NetworkPolicies de Kubernetes, container scanning, dependency scanning (Dependabot, Snyk free), TLS interno entre servicios.

---

### MES 4 — Producción real + capitalizar

#### Semana 14 · Backups, DR, runbooks
- **Deliverable:** backups automáticos de Postgres a S3 con retención, restore probado de verdad (no solo "el cron corre"), runbooks Markdown para 3 escenarios: "SFU caído", "TURN caído", "DB perdida".

#### Semana 15 · Costes + polish
- **Deliverable:** dashboard de costes AWS, AWS Budgets con alertas en €, optimización (right-sizing instancias, spot donde aplique), README de arquitectura del proyecto con diagrama (excalidraw o draw.io).

#### Semana 16 · Publicar
- **Deliverable:**
  1. Post 1: *"Self-hosting LiveKit on AWS: walkthrough completo con costes reales"*
  2. Post 2: *"From docker-compose to Kubernetes: voice infra production journey"*
  3. Post 3 (extra, gracias a Semana 8): *"Self-hosted SIP trunking with LiveKit: from Twilio to your own infra"*
  4. README brutal del repo: arquitectura, decisiones, costes, métricas, lecciones aprendidas.
- **Plataformas:** dev.to + LinkedIn + tu propio dominio si tienes blog.

#### Semana 17 · Aplicar de verdad
- **Deliverable:** CV y LinkedIn actualizados con el proyecto destacado. **30 candidaturas mínimo.** Mix de empresas (Madrid + remoto).
- **Targets:** consultorías técnicas serias (Codurance, Adesso, Empathy.co), startups con perfil técnico (Factorial, Glovo Tech, Job&Talent), empresas EU/US con remoto desde España (Remote, Deel-friendly), startups voice AI (Sierra, Decagon, Vapi, Retell — perfil ideal con tu stack).

---

## 7. Lo que NO está en el roadmap (a propósito)

- **Ansible, Chef, Puppet** → con Docker + K8s + Terraform sobran. Ansible es legacy en el stack moderno.
- **Service mesh (Istio, Linkerd)** → solo en empresas grandes. Irrelevante hasta perfil senior.
- **Multi-cloud** → domina AWS antes de mirar GCP/Azure.
- **Vault enterprise** → SOPS basta para los 4 meses.
- **Datadog/New Relic enterprise** → free tier de Grafana Cloud o self-hosted sobra.
- **Certificaciones AWS/CKA** → opcionales. Solo útiles si vas a consultoría grande tipo Accenture/Capgemini. Construir > certificados.
- **Microservicios, DDD, arquitectura hexagonal** → es desarrollo, no infra. Otro roadmap.

---

## 8. Reglas operativas durante los 4 meses

1. **Atascado >2 días en algo concreto:** pregunta (Discord oficial LiveKit, Reddit r/devops, foros) o salta y vuelve. No te bloquees nunca >48h.
2. **Cada viernes 30 min de retro escrita:** plantilla en `retros/YYYY-WW.md`. Qué aprendí, qué me frustró, qué viene la semana próxima.
3. **Commits diarios.** Aunque sean WIP. La gráfica de actividad de GitHub la ven los reclutadores.
4. **No te metas en Twitter/Discord de DevOps a leer opinión.** Agujero negro de tiempo. Documentación oficial > thread de influencer.
5. **Aplicar a curros desde semana 11**, no semana 17. Las primeras entrevistas calibran.
6. **Si Sonalyx te demanda urgencia, pausa 1 semana y reanuda.** No abandones, pausa.
7. **Comprar dominio propio (≈10€/año)** desde semana 7 para tener TLS real. `tunombre.dev` o similar.

---

## 9. Métricas de éxito (revisar en semanas 4, 8, 13, 17)

- [ ] Repo público con commits regulares (>4 días/semana en activo).
- [ ] Cada semana cerrada con su deliverable funcionando + README.
- [ ] Notas Markdown semanales actualizadas.
- [ ] Mes 4: 2 posts publicados con tracción mínima (50 visitas cada uno).
- [ ] Mes 4: 30+ candidaturas enviadas, ≥3 entrevistas técnicas.
- [ ] Capacidad de explicar cualquier semana del roadmap sin notas en una entrevista.

---

## 10. Recursos canónicos (referencia rápida)

| Tema | Recurso | Tipo | Coste |
|------|---------|------|-------|
| Docker | *Docker Deep Dive* (Poulton) | Libro | ~25€ |
| Redes | *High Performance Browser Networking* (Grigorik) | Libro online | Gratis (hpbn.co) |
| AWS | Adrian Cantrill SAA-C03 | Curso vídeo | ~40€ |
| Terraform | *Terraform: Up & Running* (Brikman) | Libro | ~30€ |
| Observabilidad | *Site Reliability Engineering* (Google) | Libro online | Gratis |
| Kubernetes | *Kubernetes Up & Running* (Hightower) | Libro | ~35€ |
| LiveKit | docs.livekit.io | Docs oficiales | Gratis |
| GitHub Actions | docs oficiales | Docs | Gratis |

**Inversión total en recursos: ~130€.** Despreciable comparado con 200h de tu tiempo.

---

## 11. Arquitectura del repo — un único proyecto que crece

### 11.1 Principio

El repo `livekit-infra` se estructura **por componente/responsabilidad**, no por semana. Cada semana **añade carpetas o ficheros** a la estructura compartida — nunca crea una carpeta `week-XX/` con código nuevo.

Excepción única: `week-00/` queda congelado como histórico de la exploración inicial. A partir de Semana 1 el código que hiciste en `week-00/token_server.py` se mueve a `services/token-server/` y vive ahí para siempre, evolucionando.

Las **notas semanales** (qué aprendí, qué hice) sí van en `notes/week-XX.md` — eso es documentación, no código.

### 11.2 Estructura final (al terminar Semana 17)

```
livekit-infra/
├── README.md                       # Top-level: qué es, arquitectura, cómo correr
├── .gitignore
│
├── docs/                           # Documentación viva del proyecto
│   ├── architecture.md             # Diagrama actual + decisiones clave
│   ├── decisions/                  # ADRs (1 por decisión importante)
│   │   ├── 001-aws-over-gcp.md
│   │   ├── 002-caddy-over-nginx.md
│   │   └── ...
│   ├── costs.md                    # Costes mensuales reales por entorno
│   └── lessons-learned.md          # Gotchas, sorpresas, anti-patrones encontrados
│
├── notes/                          # Notas semanales (qué aprendí)
│   ├── week-00.md
│   ├── week-01.md
│   └── ...
│
├── retros/                         # Retros viernes
│   ├── 2026-W18.md
│   └── ...
│
├── services/                       # Código propio (Python/Go)
│   ├── token-server/               # Genera JWTs para clientes
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile              # Dockerfile propio del servicio
│   │   └── tests/
│   └── worker/                     # Worker conectado a rooms (audio analysis, etc)
│       ├── main.go
│       ├── go.mod
│       └── Dockerfile
│
├── client/                         # Frontend web mínimo (HTML+JS plano)
│   ├── index.html
│   ├── app.js
│   ├── style.css
│   └── Dockerfile                  # nginx alpine sirviendo estáticos
│
├── docker/                         # Orquestación local
│   ├── docker-compose.yml          # Stack completo para desarrollo
│   ├── docker-compose.override.yml # Override local opcional
│   └── livekit.yaml                # Config del LiveKit server
│
├── terraform/                      # Infraestructura como código
│   ├── backend.tf                  # S3 + DynamoDB lock
│   ├── modules/
│   │   ├── network/                # VPC, subnets, route tables
│   │   ├── compute/                # EC2 / EKS según fase
│   │   ├── data/                   # RDS Postgres, ElastiCache Redis
│   │   ├── livekit/                # Módulo principal compuesto
│   │   └── observability/          # Prometheus + Grafana
│   └── envs/
│       ├── staging/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── terraform.tfvars
│       └── prod/
│           └── ...
│
├── k8s/                            # Kubernetes (Mes 3 en adelante)
│   ├── helm-values/
│   │   ├── livekit-staging.yaml    # values.yaml para chart oficial
│   │   └── livekit-prod.yaml
│   ├── manifests/                  # Lo que no es Helm (servicios propios)
│   │   ├── token-server.yaml
│   │   ├── worker.yaml
│   │   └── ingress.yaml
│   ├── policies/                   # NetworkPolicies, PodSecurity
│   │   └── network-policies.yaml
│   └── argocd/                     # GitOps (Semana 11+)
│       └── applications/
│
├── observability/                  # Configs de stack de monitoring
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   └── alerts.yml
│   ├── grafana-dashboards/         # JSON exportados
│   │   ├── livekit-overview.json
│   │   └── infra-overview.json
│   └── loki/
│       └── loki-config.yaml
│
├── runbooks/                       # Cómo arreglar incidentes
│   ├── sfu-down.md
│   ├── turn-down.md
│   ├── db-recovery.md
│   └── high-packet-loss.md
│
├── scripts/                        # Utilidades operativas
│   ├── load-test.sh
│   ├── backup-restore.sh
│   └── rotate-secrets.sh
│
├── .github/
│   └── workflows/                  # CI/CD
│       ├── ci.yml                  # Tests + lint en PR
│       ├── docker-build.yml        # Build + push imágenes
│       └── deploy.yml              # Deploy a cluster
│
└── week-00/                        # CONGELADO — exploración inicial
    ├── notes.md
    ├── server-run.md
    ├── token_server.py             # Versión inicial (luego movida a services/)
    └── client/
        └── index.html
```

### 11.3 Cuándo aparece cada parte (mapping semanas → estructura)

| Semana | Qué se añade al repo |
|--------|----------------------|
| **0** | `README.md` mínimo + carpeta `week-00/` con server local + token server + cliente HTML. `notes/week-00.md`. |
| **1** | Mueve `week-00/token_server.py` → `services/token-server/main.py`. Crea `Dockerfile` por servicio. `client/` con HTML servido por nginx. `docker/docker-compose.yml` orquesta todo. `week-00/` queda congelado. |
| **2** | `docs/architecture.md` con diagrama de red (DNS → TLS → WebSocket → media). Sin código nuevo. |
| **3** | Sin estructura nueva. Screenshots de AWS console en `notes/week-03.md`. |
| **4** | Aparece `terraform/` plano (todo en un solo dir). Estado local. LiveKit corriendo en EC2. |
| **5** | `terraform/` se reorganiza en `modules/` + `envs/staging` + `envs/prod`. `backend.tf` con state remoto. Aparece `docs/decisions/` con primer ADR. |
| **6** | `observability/` con Prometheus + Grafana + Loki + alertas. Dashboard JSON exportado. |
| **7** | `docker/livekit.yaml` se actualiza con TURN config. Configs de Caddy. Compras dominio (`tunombre.dev`). |
| **8** | Aparece `services/sip-dispatcher/`, `docker/sip.yaml`, runbooks SIP. Trunk en Telnyx (o equivalente) registrado y rutado. **Primera llamada telefónica real funciona.** |
| **9** | `scripts/load-test.sh`. Resultados en `docs/load-test-results.md`. Tuning de sysctl documentado en runbook. |
| **10** | Aparece `k8s/` con cluster k3s y manifests para 2-3 servicios tontos (no LiveKit aún). |
| **11** | `k8s/helm-values/` con LiveKit oficial. `k8s/manifests/` con tus servicios propios. Empiezas a aplicar a curros. |
| **12** | `.github/workflows/` con CI/CD. `k8s/argocd/` con apps. |
| **13** | `k8s/policies/` con NetworkPolicies. `scripts/rotate-secrets.sh`. Trivy en CI. |
| **14** | `runbooks/` con escenarios reales. `scripts/backup-restore.sh` probado. |
| **15** | `docs/costs.md` con números reales. `docs/architecture.md` actualizado con diagrama final. |
| **16** | 2-3 posts publicados (links en README). README brutal del repo terminado. |
| **17** | Sin estructura nueva. CV/LinkedIn actualizados, candidaturas. |

### 11.4 Reglas de oro de la estructura

1. **Una sola fuente de verdad por componente.** El Dockerfile del token-server vive en `services/token-server/Dockerfile`, no en `docker/`. La carpeta `docker/` es solo para orquestación (compose, configs compartidas).
2. **Lo que es código de servicio → `services/`.** Lo que es infra (declarativo) → `terraform/` o `k8s/`. Lo que es operación → `scripts/` o `runbooks/`.
3. **Nunca dupliques configs.** Si una variable se usa en varios sitios, va en `terraform.tfvars` o secrets manager, no copy-paste.
4. **`week-00/` no se toca después de Semana 1.** Es un fósil intencional para que en 6 meses te acuerdes de cómo era el primer día. Cualquier evolución va a la estructura real.
5. **Notas y retros son markdown plano.** No te montes Obsidian/Notion separado. El repo es la fuente de verdad de tu aprendizaje también.
6. **Cada PR a `main` cierra una semana o un sub-deliverable.** No mergees commits sueltos. Eso entrena la disciplina de PRs decentes que vas a necesitar en curros.

---

**Siguiente paso (hoy):** crear el repo `livekit-infra` en GitHub, copiar este roadmap dentro, hacer primer commit. Mañana empieza Semana 1.
