"""add-user-and-relations

Revision ID: 7d983f32e3e9
Revises: 
Create Date: 2025-02-08 16:20:59.947810

"""
from typing import Sequence, Union
from app.models.user import UserType, PersonType, JuristicPersonType, GenderType, EducationType, EthnicityType, SocialLinkType, DesabilityType

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d983f32e3e9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column('user_type', sa.Enum(UserType, name='user_type'), nullable=False),
        sa.Column('person_type', sa.Enum(PersonType, name='person_type'), nullable=False),
        sa.Column('full_name', sa.String, nullable=False),
        sa.Column('email', sa.String, unique=True, nullable=False),
        sa.Column('cell_phone', sa.String, unique=True, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('is_profile_completed', sa.Boolean, default=False),
        sa.Column('is_verified', sa.Boolean, default=False),
        sa.Column('gender', sa.Enum(GenderType, name='gender_type'), nullable=True),
        sa.Column('ethnicity', sa.Enum(EthnicityType, name='ethnicity_type'), nullable=True),
        sa.Column('education', sa.Enum(EducationType, name='education_type'), nullable=True)
    )

    op.create_table(
        'physical_persons',
        sa.Column('id', sa.Integer, sa.ForeignKey('users.id'), primary_key=True),
        sa.Column('cpf', sa.String, unique=True, nullable=False),
        sa.Column('rg', sa.String, nullable=False),
        sa.Column('birth_date', sa.Date, nullable=False),
        sa.Column('disability', sa.Enum(DesabilityType, name='desability_type'), default=False),
    )

    op.create_table(
        'juristic_persons',
        sa.Column('id', sa.Integer, sa.ForeignKey('users.id'), primary_key=True),
        sa.Column('cnpj', sa.String, unique=True, nullable=False),
        sa.Column('company_name', sa.String, nullable=False),
        sa.Column('fantasy_name', sa.String, nullable=True),
        sa.Column('legal_representative', sa.String, nullable=False),
        sa.Column('legal_representative_cpf', sa.String, nullable=False),
        sa.Column('foundation_date', sa.Date, nullable=False),
        sa.Column('juristic_person_type', sa.Enum(JuristicPersonType, name='juristic_person_type'), nullable=False),
    )

    op.create_table(
        'social_links',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('type', sa.Enum(SocialLinkType, name='social_link_type'), nullable=False),
        sa.Column('url', sa.String, nullable=False),
    )

    op.create_table(
        'addresses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('postal_code', sa.String, nullable=False),
        sa.Column('city', sa.String, nullable=False),
        sa.Column('state', sa.String, nullable=False),
        sa.Column('street', sa.String, nullable=False),
        sa.Column('number', sa.String, nullable=False),
        sa.Column('neighborhood', sa.String, nullable=False),
        sa.Column('complement', sa.String, nullable=True),
        sa.Column('zone', sa.String, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('addresses')
    op.drop_table('social_links')
    op.drop_table('juristic_persons')
    op.drop_table('physical_persons')
    op.drop_table('users')
