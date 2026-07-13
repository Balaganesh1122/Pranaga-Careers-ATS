class RecommendationEngine:

    @staticmethod
    def predict(score: int):

        if score >= 85:
            recommendation = "Strongly Recommend"

        elif score >= 70:
            recommendation = "Recommend"

        elif score >= 50:
            recommendation = "Consider"

        else:
            recommendation = "Reject"

        if score >= 85:
            summary = (
                "Excellent match for the role. Candidate possesses most of the required technical skills."
            )

        elif score >= 70:
            summary = (
                "Good overall match. Candidate meets the majority of the required skills with minor gaps."
            )

        elif score >= 50:
            summary = (
                "Partial match. Candidate has several relevant skills but important gaps remain."
            )

        else:
            summary = (
                "Low match. Candidate is missing several critical skills required for this role."
            )

        return {
            "recommendation": recommendation,
            "summary": summary,
        }

    # Backward compatibility
    @staticmethod
    def generate(score: int):
        return RecommendationEngine.predict(score)