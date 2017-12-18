from rest_framework import serializers

from main.models import Child, Parents, Journal


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = '__all__'


class ParentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parents
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    child_id = serializers.IntegerField()
    pick_up_time = serializers.DateTimeField(required=False)

    class Meta:
        model = Journal
        fields = ('child_id', 'pick_up_time', 'bring_time', )


class ChildParentsSerializer(serializers.ModelSerializer):
    mother = serializers.CharField(write_only=True)
    father = serializers.CharField(write_only=True)

    class Meta:
        model = Child
        fields = ('mother', 'father',)

    def update(self, instance, validated_data):
        Parents.objects.create(
            **validated_data,
            child=instance,

        )
        return instance
