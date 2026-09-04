from utils.logger_service import LoggerService
from utils.exceptions import ServiceError
from utils.time import utc_now

class Sellr:
    def __init__(self):
        self.log = LoggerService("Sellr")
        self.engine = SellrEngine()

    def post(self, item):
        start = utc_now()
        try:
            result = self.engine.post(item)
            self.log.info("post complete")
            self.log.info(f"post_time={(utc_now() - start).total_seconds()}")
            return result
        except Exception as e:
            self.log.error(str(e))
            raise ServiceError(str(e))

    def edit(self, item_id, updates):
        start = utc_now()
        try:
            result = self.engine.edit(item_id, updates)
            self.log.info("edit complete")
            self.log.info(f"edit_time={(utc_now() - start).total_seconds()}")
            return result
        except Exception as e:
            self.log.error(str(e))
            raise ServiceError(str(e))

    def delete(self, item_id):
        start = utc_now()
        try:
            result = self.engine.delete(item_id)
            self.log.info("delete complete")
            self.log.info(f"delete_time={(utc_now() - start).total_seconds()}")
            return result
        except Exception as e:
            self.log.error(str(e))
            raise ServiceError(str(e))

    async def post_async(self, item):
        return await self.engine.post_async(item)

    async def edit_async(self, item_id, updates):
        return await self.engine.edit_async(item_id, updates)

    async def delete_async(self, item_id):
        return await self.engine.delete_async(item_id)

    def post_batch(self, items):
        return [self.post(i) for i in items]

    def edit_batch(self, edits):
        return [self.edit(e["id"], e["updates"]) for e in edits]

    def delete_batch(self, ids):
        return [self.delete(i) for i in ids]
