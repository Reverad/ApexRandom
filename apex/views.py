from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Legend
from .serializers import LegendSerializer
import random


# Create your views here.
def legend_list(request):
    legends = Legend.objects.all().order_by('class_type')
    legend_classes = {}
    for legend in legends:
        if legend.class_type not in legend_classes:
            legend_classes[legend.class_type] = []
        legend_classes[legend.class_type].append(legend)
    return render(request, 'apex/legend_list.html', {'legend_classes': legend_classes})


def random_legend(request):
    legends = list(Legend.objects.all())
    legend = random.choice(legends) if legends else None
    return render(request, 'apex/random_legend.html', {'legend': legend})


@api_view(['GET'])
def legend_list_api(request):
    legends = Legend.objects.all()
    serializer = LegendSerializer(legends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def random_legend_api(request):
    legends = Legend.objects.all()
    if legends:
        legend = random.choice(legends)
        serializer = LegendSerializer(legend)
        return Response(serializer.data)
    return Response({'error': 'No Legends'}, status=404)
