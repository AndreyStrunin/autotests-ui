from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_exercise_button = Button(
            page, 'create-course-exercise-{exercise_index}-box-toolbar-delete-exercise-button', 'Delete exercise')
        self.subtitle_input = Text(page, 'create-course-exercise-{exercise_index}-box-toolbar-subtitle-text',
                                   'Exercise Subtitle')
        self.title_input = Input(page, 'create-course-exercise-form-title-{exercise_index}-input', 'Exercise Title')
        self.description_input = Input(page, 'create-course-exercise-form-description-{exercise_index}-input',
                                       'Exercise Description')

    def click_delete_button(self, exercise_index: int):
        self.delete_exercise_button.click(exercise_index=exercise_index)

    def check_visible(self, exercise_index: int, title: str, description: str):
        self.subtitle_input.check_visible(exercise_index=exercise_index)
        self.subtitle_input.check_have_text(f'#{exercise_index + 1} Exercise', exercise_index=exercise_index)

        self.title_input.check_visible(exercise_index=exercise_index)
        self.title_input.check_have_value(title, exercise_index=exercise_index)

        self.description_input.check_visible(exercise_index=exercise_index)
        self.description_input.check_have_value(description, exercise_index=exercise_index)

    def fill_create_form(self, exercise_index: int, title: str, description: str):
        self.title_input.fill(title, exercise_index=exercise_index)
        self.title_input.check_have_value(title, exercise_index=exercise_index)

        self.description_input.fill(description, exercise_index=exercise_index)
        self.description_input.check_have_value(description, exercise_index=exercise_index)
