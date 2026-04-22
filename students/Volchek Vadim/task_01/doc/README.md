<p align="center">Ministry of Education of the Republic of Belarus</p>
<p align="center">Brest State Technical University</p>
<p align="center">Department IIT</p>
<br><br><br><br><br><br>
<p align="center"><strong>Laboratory work #1</strong></p>
<p align="center"><strong>Course:</strong> "Internet Systems Design"</p>
<p align="center"><strong>Theme:</strong> "Transaction scenario: use-case and responsibility boundaries"</p>
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

Model bug creation transaction, identify failures and compensations.

---

## Variant 11 - Bug tracker "Ne bag, a ficha?"

**Pitch:** Otlichaem bagi ot magii.  
**Core domain:** Projects, Bugs, Priorities, Statuses, Assignment, Attachments.

---

## Work progress

### 1. Artifact structure

```text
task_01/
??? doc/README.md
??? src/
    ??? use-case.md
    ??? analysis.md
    ??? scenarios.feature
    ??? diagrams/
        ??? sequence-happy.puml
        ??? sequence-error-validation.puml
```

### 2. Main use-case

Flow:
1. Reporter sends `CreateBug`.
2. Service validates project and priority.
3. System creates bug with `OPEN` status.
4. Data is saved in storage.
5. Event `BugCreated` is published.

### 3. Error flows

- `PROJECT_NOT_FOUND`
- `INVALID_PRIORITY`
- Event publish failure (outbox + retry).

## Grading criteria

| Criteria | Points | Done |
|----------|--------|------|
| Use-case and alternatives | 20 | Yes |
| Sequence diagrams | 25 | Yes |
| Gherkin scenarios | 20 | Yes |
| Responsibility analysis | 20 | Yes |
| Report quality | 15 | Yes |
| **Total** | **100** | |

## Conclusion

Lab requirements are completed for variant 11. Report is formatted in unified style and ready for review.

---

**Date:** 22.04.2026  
**Grade:** _____________  
**Teacher signature:** _____________

