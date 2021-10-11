from puzzle.models import Puzzle
from django.utils import timezone
import uuid


def make_Puzzles(num_create):
    for i in range(num_create):
        Puzzle.objects.create(
            title='test' + str(i),
            size=2,
            created_at=timezone.now(),
            update_at=timezone.now(),
            picture_url="test.png",
            user_id=str(uuid.uuid4())
        )
