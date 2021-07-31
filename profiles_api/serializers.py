from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    age  = serializers.CharField(max_length=5)



# As far as I can understand, serializers are similar to a 'input' statements we use in Python.
# Or we can compare this with a text or other input fields we use Tkinter as well.
# So in short, we will have a field with 'Name' header where a user can insert values inside the field.
# And we are allowing user to insert value with maximum 10 characters length.
