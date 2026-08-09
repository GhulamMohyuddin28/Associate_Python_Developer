# User Registration Module

A basic modular Python project that validates user input (`name`, `email`, `password`) using helper validation functions, then registers the user if all checks pass.

## 🧩 Validators

These are the **helper functions** that check individual fields. Each returns `True` or `False`.

## User

This is where `validate_user()` **imports** the helper functions and checks each one. If a check fails, it raises a `ValueError` with a descriptive message. `register_user()` then calls `validate_user()`, catches any `ValueError`, and either returns `False` or a user dictionary.

## 🔍 How It Works — Step by Step

1. **`validate_name()`, `validate_email()`, `validate_password()`** each check ONE piece of data and return `True`/`False`.
2. **`validate_user()`** imports and calls all three helpers, one by one:
   - If a helper returns `False`, it immediately `raise`s a `ValueError` with a clear message describing *what* failed.
   - If all three pass, it returns `True`.
3. **`register_user()`** wraps `validate_user()` in a `try/except`:
   - If `validate_user()` raises `ValueError`, the `except` block catches it, prints/logs the reason (for debugging), and returns `False`.
   - If no exception is raised, it builds and returns a dictionary with `name`, `email`, and `password`.
