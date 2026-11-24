import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page, 'course-widget-title-text', 'Title')
        self.image = Image(page, 'course-preview-image', 'Preview')
        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'Estimated time')

    @allure.step('Check course view visible at position {position}')
    def check_visible(self, position: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.image.check_visible(nth=position)

        self.title.check_visible(nth=position)
        self.title.check_have_text(title, nth=position)

        self.max_score_text.check_visible(nth=position)
        self.max_score_text.check_have_text(f'Max score: {max_score}', nth=position)

        self.min_score_text.check_visible(nth=position)
        self.min_score_text.check_have_text(f'Min score: {min_score}', nth=position)

        self.estimated_time_text.check_visible(nth=position)
        self.estimated_time_text.check_have_text(f'Estimated time: {estimated_time}', nth=position)
