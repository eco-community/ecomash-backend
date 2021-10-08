from tortoise import fields, models


class User(models.Model):
    """
    The User model
    """

    id = fields.CharField(pk=True, max_length=255)
    name = fields.CharField(max_length=255)
    kills = fields.IntField(default=0)
    deaths = fields.IntField(default=0)
    score = fields.IntField(default=0)
    flag = fields.CharField(max_length=50, null=True)
    last_played = fields.DatetimeField()
    # lifetime stats for logged in users
    total_kills = fields.IntField(default=0)
    total_deaths = fields.IntField(default=0)
    total_score = fields.IntField(default=0)

    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
