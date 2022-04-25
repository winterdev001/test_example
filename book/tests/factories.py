import factory
from book.models import Book, Variation

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
        
    title = "Django Book1"
    memo = "Good"
    
    @factory.post_generation
    def with_variations(self, create, extracted, **kwargs):
        if extracted is not None:
            VariationFactory.create(kind="paper kind",book=self)
    
class VariationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Variation
        
    kind = "PDF"
    book = factory.SubFactory(BookFactory)