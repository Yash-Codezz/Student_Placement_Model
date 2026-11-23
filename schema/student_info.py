# === Importing Libraries ==============================

from pydantic import BaseModel, Field, field_validator

from typing import Annotated, Literal


# === Pydantic Model ==============================

class StudentInfo(BaseModel):

    branch: Annotated[Literal['CSE', 'IT', 'CE', 'ME', 'EE', 'ECE', 'Chemical'], Field(..., description='Student engineering branch', example='CSE')]
    college_tier: Annotated[Literal['Tier-1', 'Tier-2', 'Tier-3'], Field(..., description='Student College Tier', example='Tier-1')]
    cgpa: Annotated[float, Field(..., gt=0, lt=10, description='Student current CGPA', example=8.5)]
    backlogs: Annotated[int, Field(..., description='Any Backlogs of Student', example=0)]
    coding_skills: Annotated[float, Field(..., gt=0, description='How good is student at Coding', example=8.0)]
    dsa_score: Annotated[float, Field(..., gt=0, lt=10, description='How Good is Student DSA', example=8.0)]
    aptitude_Score: Annotated[float, Field(..., gt=0, lt=10, description='How good is Student at aptitude', example=8.0)]
    communication_skills: Annotated[float, Field(..., gt=0, lt=10, description='Student Communication Skills', example=7.5)]
    ml_knowledge: Annotated[float, Field(..., lt=10, description='How good is student at machine learning', example=9.0)]
    system_design: Annotated[float, Field(..., lt=10, description='How well student know about system design', example=7.5)]
    internships: Annotated[int, Field(..., description='How many internships student has done', example=1)]
    projects_count: Annotated[int, Field(..., description='Number of projects completed', example=3)]
    certifications: Annotated[int, Field(..., description='Number of certifications earned', example=2)]
    hackathons: Annotated[int, Field(..., description='How many hackathons student has participated', example=1)]
    open_souce_contributions: Annotated[int, Field(..., description='Number of open-source contributions', example=1)]
    extracurriculars: Annotated[int, Field(..., description='Is student involved in extracurriculars', example=1)]

    @field_validator('branch', mode='before')
    @classmethod
    def normalize_branch(cls, branch: str) -> str:

        branch = branch.strip()
        
        return branch

    @field_validator('college_tier', mode='before')
    @classmethod
    def noramlize_collegeTier(cls, college_tier: str) -> str:

        college_tier = college_tier.strip().capitalize()

        return college_tier