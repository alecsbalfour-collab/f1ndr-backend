class PostConfig:
    def defaults(self) -> dict:
        return {
            "max_length": 500,
            "allow_images": True,
            "allow_links": True,
        }


post_config = PostConfig()
