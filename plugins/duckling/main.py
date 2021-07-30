class DucklingAbstractClass:
    def get_struct_info(self) -> tuple:
        # result = {
        #     "brand_id": 48,
        #     "city_id": 1
        # }
        brand_id = 48
        city_id = 1
        self.process()
        return brand_id, city_id

    def process(self):
        pass
