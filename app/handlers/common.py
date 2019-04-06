from jinja2 import Environment, FileSystemLoader, TemplateNotFound

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def get_argument(self, name, strip=True):

        return self._get_argument(name, self.request.arguments, strip)

    def _get_argument(self, name, source, strip=True):
        args = self._get_arguments(name, source, strip=strip)
        if not args:
            return ()
        return args[-1]

    def render(self, template_name, **kwargs):
        template_dirs = []
        if self.settings.get('template_path', ''):
            template_dirs.append(self.settings['template_path'])
        env = Environment(loader = FileSystemLoader(template_dirs))

        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        
        content = template.render(kwargs)
        
        return content

    def get_current_user(self):
        
        return self.get_secure_cookie("username")


