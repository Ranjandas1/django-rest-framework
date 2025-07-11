
from rest_framework import serializers
from .models import Car,WheelForm, WheelField, bogieDetailsForm, bogieChecksheetForm, bmbcChecksheetForm ,bogieForm

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class WheelFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelField
        exclude = ['form'] 

class WheelFormSerializer(serializers.ModelSerializer):
    fields = WheelFieldSerializer()

    class Meta:
        model = WheelForm
        fields = ['form_number', 'submitted_by', 'submitted_date', 'fields']

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        form = WheelForm.objects.create(**validated_data)
        WheelField.objects.create(form=form, **fields_data)
        return form

    def update(self, instance, validated_data):
        fields_data = validated_data.pop('fields', None)

        instance.form_number = validated_data.get('form_number', instance.form_number)
        instance.submitted_by = validated_data.get('submitted_by', instance.submitted_by)
        instance.submitted_date = validated_data.get('submitted_date', instance.submitted_date)
        instance.save()

        if fields_data:
            field_instance, created = WheelField.objects.get_or_create(form=instance)
            for key, value in fields_data.items():
                setattr(field_instance, key, value)
            field_instance.save()

        return instance


class bogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bogieDetailsForm
        exclude = ['form']

class bogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = bogieChecksheetForm
        exclude = ['form']

class bmbcChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = bmbcChecksheetForm
        exclude = ['form']

class bogieSerializer(serializers.ModelSerializer):
    bogieDetails = bogieDetailsSerializer()
    bogieChecksheet = bogieChecksheetSerializer()
    bmbcChecksheet = bmbcChecksheetSerializer()

    class Meta:
        model = bogieForm
        fields = ['form_number', 'submitted_by', 'submitted_date', 'bogieDetails', 'bogieChecksheet', 'bmbcChecksheet']

    def create(self, validated_data):
        bogie_details_data = validated_data.pop('bogieDetails')
        bogie_checksheet_data = validated_data.pop('bogieChecksheet')
        bmbc_checksheet_data = validated_data.pop('bmbcChecksheet')

        form = bogieForm.objects.create(**validated_data)

        bogieDetailsForm.objects.create(form=form, **bogie_details_data)
        bogieChecksheetForm.objects.create(form=form, **bogie_checksheet_data)
        bmbcChecksheetForm.objects.create(form=form, **bmbc_checksheet_data)
        return form
