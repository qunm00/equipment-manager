ports:
    - pg-admin: 5000
    - web: 3000
    - api: 8000

Notes:
    - Employee CRUD:
        - create method doesn't return messages where back-end fails to validate duplicated fields.
        - form position is off. need to remove max-height from .v-overlay__content
    - Equipment CRUD:
        - Three tables: devices, devices categories, employees.
        - Where to put search bar and category dropdown?
            - app-bar needs if else
            - each view has its own toolbars