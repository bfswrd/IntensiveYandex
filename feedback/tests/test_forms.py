from django.test import TestCase
from django.urls import reverse

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackFormTests(TestCase):
    def setUp(self) -> None:
        self.form = FeedbackForm()

    def test_text_label_form(self):
        name_label = self.form.fields["text"].label
        self.assertEqual(name_label, Feedback.text.field.verbose_name)

    def test_text_help_text_form(self):
        help_text = self.form.fields["text"].help_text
        self.assertEqual(help_text, Feedback.text.field.help_text)

    def test_create_feedback(self):
        items_count = Feedback.objects.count()
        form_data = {
            "text": "asdfqwer"
        }
        response = self.client.post(reverse("feedback:feedback"),
                                    data=form_data)

        self.assertRedirects(response, reverse("feedback:feedback"))
        self.assertEqual(Feedback.objects.count(), items_count + 1)

        self.assertTrue(
            Feedback.objects.filter(
                text="asdfqwer"
            )
        )
