from sqlalchemy.orm import Session

from db.models.model_comment import Comments


def add_comment(
    db: Session, blog_id: int, comment: str, user_id, comment_id: int | None = None
):
    new_comment = Comments(
        comment=comment, user_id=user_id, blog_id=blog_id, parent_id=comment_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_comment(db: Session, comment_id: int):
    print(comment_id)
    comment = db.query(Comments).filter(Comments.id == comment_id).first()

    return comment
