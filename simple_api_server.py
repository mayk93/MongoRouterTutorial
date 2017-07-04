import hug
from hug_middleware_cors import CORSMiddleware

from MongoRouter.MongoRouter import MongoRouter

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

router = MongoRouter(config_file="config.json")
# router = MongoRouter()


def clean(dct):
    del dct["_id"]
    return dct


@hug.get('/data')
def post_data(*args, **kwargs):
    try:
        print("GET Args: %s" % str(args))
    except Exception as e:
        print(e)
    try:
        print("GET Kwargs: %s" % kwargs)
    except Exception as e:
        print(e)

    try:
        print(router.route("users").find())
        try:
            for _ in router.route("users").find():
                print(_)
            print("---")
            for _ in router.route("details").find({"value": {"$gt": 2}}):
                print(_)

            x = [_ for _ in router.route("users").find()]
            y = [_ for _ in router.route("details").find({"value": {"$gt": 2}})]

            print(x)
            print(y)

            import json
            try:
                print(json.dumps(x))
            except Exception as e:
                print(e)

            try:
                print(json.dumps(y))
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
        try:
            print(router.route("users"))
        except Exception as e:
            print(e)

    try:
        return [clean(_) for _ in router.route("users").find()] + \
               [clean(_) for _ in router.route("details").find({"value": {"$gt": 2}})]
    except Exception as e:
        print(e)

    return []


@hug.post('/data')
def post_data(*args, **kwargs):
    try:
        print("POST Args: %s" % str(args))
    except Exception as e:
        print(e)
    try:
        print("POST Kwargs: %s" % kwargs)
    except Exception as e:
        print(e)

    try:
        u_iod = router.route("users").insert({"name": kwargs.get("name", "unknown name")})
    except Exception as e:
        print(e)

    try:
        d_oid = router.route("details").insert({"value": kwargs.get("value", -1)})
    except Exception as e:
        print(e)

    try:
        return {"u_oid": str(u_iod), "d_oid": str(d_oid)}
    except Exception as e:
        print(e)
        return {}

