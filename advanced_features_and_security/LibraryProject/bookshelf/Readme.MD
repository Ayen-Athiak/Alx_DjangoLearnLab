# Permissions and Groups Setup

## Model Permissions

The `Book` model includes the following custom permissions:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

## Groups and Permissions

### Editors
- **Permissions**: `can_edit`, `can_create`

### Viewers
- **Permissions**: `can_view`

### Admins
- **Permissions**: `can_view`, `can_create`, `can_edit`, `can_delete`

## Enforcing Permissions

Permissions are enforced in views using the `@permission_required` decorator. Ensure that the decorator is used to restrict access based on permissions.

## Testing

- **Test Users**: Created in Django Admin and assigned to appropriate groups.
- **Testing**: Log in as users from different groups to verify that permissions are correctly enforced.

