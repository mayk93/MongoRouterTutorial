import hug
from hug_middleware_cors import CORSMiddleware

from MongoRouter.MongoRouter import MongoRouter

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

router = MongoRouter(config_file="config.json")


@hug.get('/data')
def post_data(*args, **kwargs):
    return [_ for _ in router.route("users").find()] + [_ for _ in router.route("details").find({"value": {"$gt": 2}})]


@hug.post('/data')
def post_data(*args, **kwargs):
    u_iod = router.route("users").insert({"name": kwargs.get("name", "unknown name")})
    d_oid = router.route("details").insert({"value": kwargs.get("value", -1)})

    return {"u_oid": str(u_iod), "d_oid": str(d_oid)}

