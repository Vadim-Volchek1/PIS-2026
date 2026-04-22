<p align="center">Ministry of Education of the Republic of Belarus</p>
<p align="center">Brest State Technical University</p>
<p align="center">Department IIT</p>
<br><br><br><br><br><br>
<p align="center"><strong>Laboratory work #5</strong></p>
<p align="center"><strong>Course:</strong> "Internet Systems Design"</p>
<p align="center"><strong>Theme:</strong> "Infrastructure layer: API and DB"</p>
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

Implement REST endpoints and persistence integration.

---

## Variant 11 - Bug tracker "Ne bag, a ficha?"

**Pitch:** Otlichaem bagi ot magii.  
**Core domain:** Projects, Bugs, Priorities, Statuses, Assignment, Attachments.

---

## Work progress

### 1. REST API

Implemented:
- `POST /api/bugs`
- `POST /api/bugs/{bug_id}/assign`
- `GET /api/bugs/{bug_id}`
- `GET /api/bugs`

### 2. Database setup

Docker compose prepared for local PostgreSQL.

### 3. Integration checks

HTTP create/get scenario covered by test.

## Grading criteria

| Criteria | Points | Done |
|----------|--------|------|
| REST API | 25 | Yes |
| Adapters/repository | 25 | Yes |
| DB setup | 20 | Yes |
| Integration tests | 20 | Yes |
| Report quality | 10 | Yes |
| **Total** | **100** | |

## Conclusion

Lab requirements are completed for variant 11. Report is formatted in unified style and ready for review.

---

**Date:** 22.04.2026  
**Grade:** _____________  
**Teacher signature:** _____________

