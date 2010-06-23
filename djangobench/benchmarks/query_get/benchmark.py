from djangobench.utils import run_benchmark
from query_get.models import Book

def benchmark():
    Book.objects.get(id=1)

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.get() call.',
    }
)
