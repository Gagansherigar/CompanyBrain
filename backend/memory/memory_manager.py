from memory.memory_store import (
    store_memory
)


class MemoryManager:

    def save_memory(
        self,
        embedding,
        payload
    ):

        store_memory(
            embedding,
            payload
        )