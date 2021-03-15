from src.models.bases import Indexed


class LeitnerSystem:

    @staticmethod
    def leitner_algorithm(db: Indexed, user_id: str, required_amount_of_questions: int) -> tuple:
        table_questions = db.database.execute(
            f'''
                select "single_task_id", "date", "last_delay"
                from "single_task_stat"
                where "user_id" = {user_id}
                order by "last_delay";
                
                select "multi_task_id", "date", "last_delay"
                from "multi_task_stat"
                where "user_id" = {user_id}
                order by "last_delay";
                
                select "map_task_id", "date", "last_delay"
                from "map_task_stat"
                where "user_id" = {user_id}
                order by "last_delay";
            '''
        )
        questions_id = table_questions[
            0:
            required_amount_of_questions + 1
            if required_amount_of_questions + 1 < len(table_questions)
            else len(table_questions)
        ]
        return questions_id
