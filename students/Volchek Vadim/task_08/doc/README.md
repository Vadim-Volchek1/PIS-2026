<p align="center">Ministry of Education of the Republic of Belarus</p>
<p align="center">Brest State Technical University</p>
<p align="center">Department IIT</p>
<br><br><br><br><br><br>
<p align="center"><strong>Laboratory work #8</strong></p>
<p align="center"><strong>Course:</strong> "Internet Systems Design"</p>
<p align="center"><strong>Theme:</strong> "Microservices and event-driven integration"</p>
<br><br><br><br><br><br>
<p align="right"><strong>Vypolnil:</strong></p>
<p align="right">Student 3 kursa</p>
<p align="right">Volchek Vadim Aleksandrovich</p>
<p align="right"><strong>Proveril:</strong></p>
<p align="right">Nesyuk A.N.</p>
<br><br><br><br><br>
<p align="center"><strong>Brest 2026</strong></p>

---

## Goal

Decompose system to bounded contexts and event bus.

---

## Variant 11 - Bug tracker "Ne bag, a ficha?"

**Pitch:** Otlichaem bagi ot magii.  
**Core domain:** Projects, Bugs, Priorities, Statuses, Assignment, Attachments.

---

## Work progress

### 1. Services

- request-service
- group-service
- notification-service

### 2. Event bus

RabbitMQ routes `bug.created` and `bug.assigned` events.

### 3. Deployment

Docker compose starts all services and broker.

### 4. Scalability

Each service can be scaled independently.

## Grading criteria

| Criteria | Points | Done |
|----------|--------|------|
| Service decomposition | 25 | Yes |
| Event bus | 25 | Yes |
| Gateway/routing | 20 | Yes |
| Docker setup | 20 | Yes |
| Report quality | 10 | Yes |
| **Total** | **100** | |

## Conclusion

Lab requirements are completed for variant 11. Report is formatted in unified style and ready for review.

---

**Date:** 22.04.2026  
**Grade:** _____________  
**Teacher signature:** _____________

