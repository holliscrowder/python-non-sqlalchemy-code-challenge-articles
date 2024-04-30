class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("author must be of class type Author")
        else:
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be of class type Magazine")
        else:
            self._magazine = magazine

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if (
            isinstance(title, str)
            and 5 <= len(title) <= 50
            and not hasattr(self, "_title")
        ):
            self._title = title


class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [
            article
            for article in Article.all
            if isinstance(article, Article) and article.author == self
        ]

    def magazines(self):
        return list(
            {
                article.magazine
                for article in Article.all
                if isinstance(article.magazine, Magazine) and article.author == self
            }
        )

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(
            {
                article.magazine.category
                for article in Article.all
                if article.author == self
            }
        )
        if len(topics) > 0:
            return topics
        return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [
            article
            for article in Article.all
            if isinstance(article, Article) and article.magazine == self
        ]

    def contributors(self):
        return list(
            {
                article.author
                for article in Article.all
                if isinstance(article.author, Author) and article.magazine == self
            }
        )

    def article_titles(self):
        articles = [
            article.title for article in Article.all if article.magazine == self
        ]
        if len(articles) > 0:
            return articles
        return None

    def contributing_authors(self):
        authors = [
            article.author
            for article in Article.all
            if isinstance(article.author, Author) and article.magazine == self
        ]
        more_than_two_articles = []
        for author in authors:
            if authors.count(author) > 2:
                more_than_two_articles.append(author)

        if len(more_than_two_articles) > 0:
            return more_than_two_articles
        return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
