
import scrapy
from ..items import MycmescrapeItem

class CecourseSpider(scrapy.Spider):
    name = 'ceCourse'
    start_urls = ['https://www.mycme.com/recognizing-the-many-faces-of-lupus-multidisciplinary-perspectives-for-individualized-treatment-and-management-micro-module-4-of-4/activity/6427/']

    def parse(self, response):
        items = MycmescrapeItem()
        course_title = response.css("#activityTitle::text").extract()
        items['course_title'] = course_title
        course_format = [response.css(".alpha div.activityContentSubHeadCol::text").extract_first().strip()]
        items['course_format'] = course_format
        time_to_complete = response.css("#divEstimatedTime::text").extract()
        items['time_to_complete'] = time_to_complete
        released = response.css("#activityPubDate::text").extract()
        items['released'] = released
        expires = response.css("#activityExpDate::text").extract()
        items['expires'] = expires
        credit = response.css(".gridcredMod .credFontset::text").extract()
        items['credit'] = credit
        provider = response.css(".dsThird::text").extract()
        items['provider'] = provider
        supporter = response.css(".decript.reduceMargTopBott::text").extract()
        items['supporter'] = supporter
        description = response.css(".grid_row+ .grid_row .addTopMarg.value::text").extract()
        items['description'] = description
        audience = response.css(".grid_row+ .grid_row .addTopMarg.value::text").extract()[2]
        items['audience'] = audience
        objectives = response.css(".grid_row+ .grid_row .addTopMarg.value::text").extract()[3]
        items['objectives'] = objectives 
        faculty = response.css(".facultyDesc::text").extract()
        items['faculty'] = faculty
        credit_type = response.css(".gridtypeMod em::text").extract()
        items['credit_type'] = credit_type
        accreditation = response.css(".gridtypeMod+ .creditGrid_2 .credFontset::text").extract()
        items['accreditation'] = accreditation
        designation = response.css(".marginRightZero .credFontset::text").extract()
        items['designation'] = designation
        yield items