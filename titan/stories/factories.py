import factory

from factory import fuzzy

from titan.stories.models import Story, StoryState


class StoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Story

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("text")
    state = fuzzy.FuzzyChoice(StoryState.objects.all())
    points = factory.Faker("random_int", min=0, max=8)

    workspace = factory.SubFactory("titan.workspaces.factories.WorkspaceFactory")
    requester = factory.SubFactory("titan.users.tests.factories.UserFactory")
    assignee = factory.SubFactory("titan.users.tests.factories.UserFactory")

    created_at = factory.Faker("date_time_this_decade")
    updated_at = factory.Faker("date_time_this_decade")
