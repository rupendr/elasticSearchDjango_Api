import csv, io
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib import messages
from rest_framework import status, generics
from rest_framework.response import Response

from elasticSearch.models import *
from elasticSearch.serializers import Car_Serializer, FileUploadSerializer


# Create your views here.
# one parameter named request
def index(request):
    # declaring template
    template = "index.html"
    data = Car_datasets.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be same',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|", ):
        _, created = Car_datasets.objects.update_or_create(
            price=column[0],
            brand=column[1],
            model=column[2],
            year=column[3],
            title_status=column[4],
            mileage=column[5],
            color=column[6],
            vin=column[7],
            lot=column[8],
            state=column[9],
            country=column[10],
            condition=column[11],

        )
    context = {}
    return render(request, template, context)


class CsvFileUpload(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        decoded_file = file.read().decode()
        # upload_products_csv.delay(decoded_file, request.user.pk)
        io_string = io.StringIO(decoded_file)
        for column in csv.reader(io_string, delimiter=',', quotechar="|", ):
            _, created = Car_datasets.objects.update_or_create(
                price=column[0],
                brand=column[1],
                model=column[2],
                year=column[3],
                title_status=column[4],
                mileage=column[5],
                color=column[6],
                vin=column[7],
                lot=column[8],
                state=column[9],
                country=column[10],
                condition=column[11],

            )
        response = {
            'data_inserted': Car_datasets.objects.all().count(),
            'message': "request success message",
            'status_code': status.HTTP_201_CREATED,
        }
        return Response(response)


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Car_datasets.objects.all()
        serializer = Car_Serializer(snippets, many=True)
        response = {
            'message': "request success message",
            'status_code': status.HTTP_200_OK,
            'car_dataset': serializer.data
        }

        return Response(response)

    elif request.method == 'POST':
        snippets = Car_datasets.objects.all()

        serializer = Car_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data_inserted': Car_datasets.objects.all().count(),
                'message': "request success message",
                'status_code': status.HTTP_201_CREATED,
                'car_dataset': serializer.data
            }
            return Response(response)
        response = {
            'data_inserted': Car_datasets.objects.all().count(),
            'message': "request fail message",
            'status_code': status.HTTP_400_BAD_REQUEST,
            'car_dataset': serializer.errors
        }
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Car_datasets.objects.get(pk=pk)
    except Car_datasets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Car_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Car_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'document': 'pending',
                'message': "request success message",
                'status_code': status.HTTP_201_CREATED,
                'document': serializer.data
            }
            return Response(response)
        response = {
            'message': "request fail message",
            'status': status.HTTP_400_BAD_REQUEST,
            'document': serializer.errors
        }
        return Response(response)

    elif request.method == 'DELETE':
        # snippet=Car_datasets.objects.get(document_id=request.data.document_id)
        snippet.delete()
        response = {
            'document_id': 'snippet',
            'message': "request scuess message",
            'status': status.HTTP_204_NO_CONTENT,
        }
        return Response(response)

