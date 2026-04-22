<p align="center">Ministry of Education of the Republic of Belarus</p>
<p align="center">Brest State Technical University</p>
<p align="center">Department IIT</p>
<br><br><br><br><br><br>
<p align="center"><strong>Laboratory work #9</strong></p>
<p align="center"><strong>Course:</strong> "Internet Systems Design"</p>
<p align="center"><strong>Theme:</strong> "Protocol Buffers and gRPC"</p>
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

Define protobuf contract and gRPC interactions.

---

## Variant 11 - Bug tracker "Ne bag, a ficha?"

**Pitch:** Otlichaem bagi ot magii.  
**Core domain:** Projects, Bugs, Priorities, Statuses, Assignment, Attachments.

---

## Work progress

### 1. Proto contract

`src/proto/bug_service.proto` defines messages and RPC methods.

### 2. gRPC server

Supports `CreateBug`, `GetBug`, `ListActiveBugs`.

### 3. gRPC client

Demonstrates unary RPC and server-streaming calls.

### 4. Compatibility

Schema evolution uses new field numbers only.

## Grading criteria

| Criteria | Points | Done |
|----------|--------|------|
| Proto contract | 25 | Yes |
| gRPC server | 25 | Yes |
| gRPC client | 20 | Yes |
| Streaming RPC | 20 | Yes |
| Report quality | 10 | Yes |
| **Total** | **100** | |

## Conclusion

Lab requirements are completed for variant 11. Report is formatted in unified style and ready for review.

---

**Date:** 22.04.2026  
**Grade:** _____________  
**Teacher signature:** _____________

