# AI Usage

## 1. AI Tool Used

I used ChatGPT as an AI-assisted development tool during this assignment.

The AI was used for guidance, code suggestions, debugging, understanding Django concepts, and reviewing the implementation.

## 2. How AI Was Used

I used ChatGPT to help me:

- Set up the Django project and application.
- Understand Django models and relationships.
- Configure Django Admin.
- Design the box recommendation logic.
- Create the recommendation service.
- Build the basic web interface.
- Debug errors encountered during development.
- Create and improve automated test cases.
- Review the implementation and identify issues.

## 3. Prompts Given to AI

Some of the prompts/instructions I gave to ChatGPT included:

### Prompt 1 — Project setup

"I am working on a Django project for a Python/Django Hiring Assignment: AI-Assisted Box Selection System. I am new to Django. Guide me step by step."

### Prompt 2 — Recommendation logic

" Let's start the remaining part of the assignment and guide me step by step."

### Prompt 3 — Debugging

"I am getting a test failure for test_product_rotation_is_allowed. Here is my service.py and test output. Please identify the issue."

### Prompt 4 — Code review

"I have completed the core Django implementation. Please review my models.py."

### Prompt 5 — Testing

"Do I need to replace the complete class BoxRecommendationTest?"

## 4. Output Accepted

I accepted and used AI suggestions for:

- Creating the initial Django project structure.
- Creating Django models for Box, Product, Order and OrderItem.
- Registering models in Django Admin.
- Creating the box recommendation service.
- Creating the basic order-selection webpage.
- Creating automated test cases.
- Debugging the product rotation test.
- Reviewing the final implementation.
- Creating documentation structure.

The suggestions were tested locally before being considered part of the final implementation.

## 5. Output Rejected or Modified

I did not blindly accept all AI-generated code.

AI suggested to use database like Mysql but as this is a small system I choose inbuild Sqlite.

During development, I modified AI suggestions when they did not match the actual project or when testing showed that the implementation needed correction.

One example was the product rotation test. The initial expected result in the test was Medium Box, but the actual recommendation was Small Box. After checking the dimensions and recommendation logic, I corrected the test expectation because Small Box was actually a valid and cheaper option.

I also corrected the box-selection tie-breaking logic in `service.py`. The original implementation used a previously calculated `box_volume` variable in the final `min()` operation. This was changed so that the volume is calculated for each box directly during comparison.

## 6. Mistakes Identified

The following issues were identified during development:

### Indentation Error

An `IndentationError` occurred in `models.py` while editing the model methods.

The error was identified from the Django server traceback and corrected.

### Incorrect Model Import

I initially attempted:

```python
from box_selector.models import order