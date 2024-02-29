class Article:

    all = []

    def __init__(self, author, magazine, title):
        assert isinstance(author, Author), "author must be an instance of Author class"
        self.author = author
        assert isinstance(magazine, Magazine), "magazine must be an instance of Magazine class"
        self.magazine = magazine
        assert isinstance(title, str), "title must be a string"
        assert 5 <= len(title) <= 50, "title must be between 5 and 50 characters long"
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            raise AttributeError("title can't be reset")
        self._title = title
        
class Author:

    author_list = []

    def __init__(self, name):
        assert isinstance(name, str), "name must be a string"
        assert len(name) > 0, "name must be at least 1 character long" 
        self.name = name
        Author.author_list.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise AttributeError("name can't be reset")
        self._name = name

    def articles(self):
        author_articles = []
        for article in Article.all:
            if getattr(article, "author") == self:
                author_articles.append(article)
        return author_articles

    def magazines(self):
        author_magazines = []
        for article in Article.all:
            if getattr(article, "author") == self:
                if article.magazine not in author_magazines: 
                    author_magazines.append(article.magazine)
        return author_magazines

    def add_article(self, magazine, title):
        created_article = Article(self, magazine, title)
        return created_article

    def topic_areas(self):
        author_topic = []
        for article in Article.all:
            if getattr(article, "author") == self:
                if article.magazine.category not in author_topic:
                    author_topic.append(article.magazine.category)
        if len(author_topic) > 0:
            return author_topic
        else:
            return None

class Magazine:

    magazine_list = []

    def __init__(self, name, category):
        assert isinstance(name, str), "name must be a string"
        assert 2 <= len(name) <= 16, "name must be between 2 and 16 characters long"
        self.name = name
        assert isinstance(category, str), "category must be a string"
        assert len(category) > 0, "category must be at least 1 character long"
        self.category = category
        Magazine.magazine_list.append(self)

    def articles(self):
        magazine_articles = []
        for article in Article.all:
            if getattr(article, "magazine") == self:
                magazine_articles.append(article)
        return magazine_articles

    def contributors(self):
        magazine_authors = []
        for article in Article.all:
            if getattr(article, "magazine") == self:
                if article.author not in magazine_authors: 
                    magazine_authors.append(article.author)
        return magazine_authors

    def article_titles(self):
        magazine_titles = []
        for article in Article.all:
            if getattr(article, "magazine") == self:
                if article.title not in magazine_titles:
                    magazine_titles.append(article.title)
        if len(magazine_titles) > 0:
            return magazine_titles
        else:
            return None

    def contributing_authors(self):
        magazine_authors = []
        accepted_authors = []
        for article in Article.all:
            if getattr(article, "magazine") == self: 
                magazine_authors.append(article.author)
        for author in magazine_authors:
            if magazine_authors.count(author) > 2 and author not in accepted_authors:
                accepted_authors.append(author)
        if len(accepted_authors) > 0:
            return accepted_authors
        return None


# auth1 = Author("Lovecraftian")
# print(Article.all)
# mag1 = Magazine("Eldrith Lurk", "Horror")
# auth1.add_article(mag1, "aaaaaaaaah")
# print(Article.all)
# art1 = Article(Author("Junji Ito"), Magazine("Spiraling", "Horror"), "also aaaaaaaaaaaaaah")
# print(Article.all)
# print(auth1.topic_areas())