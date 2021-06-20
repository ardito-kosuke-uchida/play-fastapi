# 起動まで

環境変数

```
cp local.env .env
```

Docker Compose で起動.

```
docker-compose up -d
```

データベースをセットアップ.

```
docker-compose exec api alembic upgrade head
```


# エンティティを作成/変更したあとのマイグレーション

`app/database` 以下にあるデータベースのエンティティを変更したあとの
データベースへの反映.

マイグレーション用スクリプト作成.

```
docker-compose exec api alembic revision --autogenerate
```

DB定義に反映.

```
docker-compose exec api alembic upgrade head
```
