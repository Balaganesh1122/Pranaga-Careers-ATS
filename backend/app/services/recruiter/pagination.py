from math import ceil


class Pagination:

    @staticmethod
    def paginate(query, page: int, page_size: int):

        total = query.count()

        items = (
            query
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return {
            "items": items,
            "page": page,
            "page_size": page_size,
            "total": total,
            "pages": ceil(total / page_size) if total else 1,
        }