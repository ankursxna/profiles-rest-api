from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

        # So above the 'permissions' is the class we have imported from rest_framework.
        # permissions.SAFE_METHOD means a 'GET' method where a user can see the list of all the users or a user with specific id.
        # If the method is not 'GET' then this 'if' block wont work it directly go to the second 'return' which is at the end of this fn.
        # In second return argument, we are getting boolean True if the id of user is matching with the id of user is trying to access
        # Or else it will return value as False which means user is trying to access someother user's profile.
        # [1] Hence with this activated, it will pass True if user is just trying to call HTTP GET method to view another users' profile.
        # [2] Also it will pass True if user is making HTTP PUT or PATCH for his own profile.
