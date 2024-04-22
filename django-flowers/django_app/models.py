from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class CategoryItem(models.Model):
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    image = models.CharField(
        verbose_name="Картинка",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default="",
        max_length=300,
    )
    slug = models.SlugField(  
        verbose_name="Ссылка",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-title",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"<CategoryItem {self.title}({self.id}) = {self.slug} />"
    

class Item(models.Model):
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    description = models.TextField(
        verbose_name="Описание",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    category = models.ForeignKey(
        verbose_name="Категория",
        db_index=True,
        primary_key=False,
        unique=False,  # !TODO OneToONe=True
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=CategoryItem,
        on_delete=models.CASCADE,
    )
    image = models.TextField(
        verbose_name="Картинка URL",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )

    is_active = models.BooleanField(
        verbose_name="Активеность объявления",
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("is_active", "-title")
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        if self.is_active:
            act = "активен"
        else:
            act = "продано"
        return f"<Item {self.title}({self.id}) | {act} | {self.description[:20]} />"
    
    def is_my_rating_selection(self, user: User) -> int:
        _item = Item.objects.get(id=self.id)
        _ratings = ItemLike.objects.all().filter(item=_item)
        _my_rating = _ratings.filter(author=user)
        if len(_my_rating) > 0:
            return 1 if _my_rating[0].is_like else -1
        else:
            return 0
    

class CommentItem(models.Model):
    author = models.ForeignKey(
        verbose_name="Автор",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=User,
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        verbose_name="Объявление",
        db_index=True,
        primary_key=False,
        editable=True,
        unique=False,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Item,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Текст комментария",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    created = models.DateTimeField(
        verbose_name="дата и время создания",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )
    is_active = models.BooleanField(
        verbose_name="Актвеность",
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-created",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"<CommentItem {self.article.title}({self.id})/>"
    
class ItemLike(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=User,
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        verbose_name="Объявление",
        db_index=True,
        primary_key=False,
        editable=True,
        unique=False,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Item,
        on_delete=models.CASCADE,
    )
    is_like = models.BooleanField(
        verbose_name="Активнность лайка",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-item",)
        verbose_name = "Активнность лайка"
        verbose_name_plural = "Активнность лайка"

    def __str__(self):
        return f"<ItemRating {self.item.title}({self.is_like})/>"