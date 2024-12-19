# main.py
import asyncio
import numpy as np
from bhakti import BhaktiClient
from bhakti.database import Metric


async def main():
    client = BhaktiClient(verbose=True)
    vector = np.random.randn(1024)
    await client.create(vector=vector, document={'age': 31, 'gender': 'male'})
    await client.create_index('age')
    await client.create_index('gender')
    results = await client.find_documents_by_vector_indexed(
        query='age <= 31 && gender != "female"',
        vector=vector,
        metric=Metric.EUCLIDEAN_Z_SCORE,
        top_k=3
    )
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
