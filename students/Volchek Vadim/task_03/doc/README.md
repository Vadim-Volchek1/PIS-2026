<p align="center">Ministry of Education of the Republic of Belarus</p>
<p align="center">Brest State Technical University</p>
<p align="center">Department IIT</p>
<br><br><br><br><br><br>
<p align="center"><strong>Laboratory work #3</strong></p>
<p align="center"><strong>Course:</strong> "Internet Systems Design"</p>
<p align="center"><strong>Theme:</strong> "Domain layer: Entity, Value Object, Aggregate"</p>
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

Implement domain model and invariants.

---

## Variant 11 - Bug tracker "Ne bag, a ficha?"

**Pitch:** Otlichaem bagi ot magii.  
**Core domain:** Projects, Bugs, Priorities, Statuses, Assignment, Attachments.

---

## Work progress

### 1. Value Objects

Implemented: `BugTitle`, `Priority`, `BugStatus`, `Attachment`.

### 2. Entity and Aggregate

`Bug` as entity, `BugAggregate` as aggregate root.

### 3. Domain events

`BugAssigned` event generated on assignment.

### 4. Tests

Unit tests cover invariants and event creation.

## Grading criteria

| Criteria | Points | Done |
|----------|--------|------|
| Value objects | 25 | Yes |
| Entity/Aggregate | 25 | Yes |
| Domain events | 20 | Yes |
| Unit tests | 20 | Yes |
| Report quality | 10 | Yes |
| **Total** | **100** | |

## Conclusion

Lab requirements are completed for variant 11. Report is formatted in unified style and ready for review.

---

**Date:** 22.04.2026  
**Grade:** _____________  
**Teacher signature:** _____________

