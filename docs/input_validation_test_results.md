# Input Module – Testing Results

## 1. Objective

The input module was tested to ensure that it accepts valid evaluation data and rejects invalid inputs.

## 2. Test Cases

| Test Case | Input Condition | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC01 | Valid input without reference data | 200 – Success | 200 – Success | Passed |
| TC02 | Empty question | 400 – Bad Request | 400 – Bad Request | Passed |
| TC03 | Empty AI response | 400 – Bad Request | 400 – Bad Request | Passed |
| TC04 | Question containing only spaces | 400 – Bad Request | 400 – Bad Request | Passed |
| TC05 | Reference document provided without reference answer | 200 – Success | 200 – Success | Passed |

## 3. Testing Outcome

All five test cases were executed successfully through the FastAPI Swagger interface.

The module correctly accepts valid inputs, rejects empty required fields and supports optional reference answers and documents.

## 4. Conclusion

The input collection and validation module is functioning as expected based on the tests performed. It is ready for integration with the next stages of the AI Response Validation System.
