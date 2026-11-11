from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator(
            'input')
        self.form_description_textarea = page.get_by_test_id('create-course-form-description-input').locator(
            'textarea').first
        self.form_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.form_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def check_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        expect(self.title_input).to_be_visible()
        expect(self.title_input).to_have_value(title)

        expect(self.estimated_time_input).to_be_visible()
        expect(self.estimated_time_input).to_have_value(estimated_time)

        expect(self.form_description_textarea).to_be_visible()
        expect(self.form_description_textarea).to_have_value(description)

        expect(self.form_max_score_input).to_be_visible()
        expect(self.form_max_score_input).to_have_value(max_score)

        expect(self.form_min_score_input).to_be_visible()
        expect(self.form_min_score_input).to_have_value(min_score)

    def fill_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.title_input.fill(title)
        expect(self.title_input).to_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        expect(self.estimated_time_input).to_have_value(estimated_time)

        self.form_description_textarea.fill(description)
        expect(self.form_description_textarea).to_have_value(description)

        self.form_max_score_input.fill(max_score)
        expect(self.form_max_score_input).to_have_value(max_score)

        self.form_min_score_input.fill(min_score)
        expect(self.form_min_score_input).to_have_value(min_score)
