from enum import StrEnum

class GenderType(StrEnum):
    WOMAN_CIS = "Mulher Cisgênero"
    MAN_CIS = "Homem Cisgênero"
    WOMAN_TRANS = "Mulher Transgênero"
    MAN_TRANS = "Homem Transgênero"

class UserType(StrEnum):
    ARTIST = "Artístico"
    ADMINISTRATOR = "Administrador"
    CONTRACTOR = "Contratante"

class PersonType(StrEnum):
    PHYSICAL_PERSON = "Pessoa Física"
    JURISTIC_PERSON = "Pessoa Jurídica"

class JuristicPersonType(StrEnum):
    FOR_PROFIT = "Com Fins Lucrativos"
    NON_PROFIT = "Sem Fins Lucrativos"
    COUNCIL = "Conselho de Direitos"
    INFORMAL_GROUP = "Grupo Informal ou Coletivo"
    PUBLIC_ORGANIZATION = "Organização Pública"

class EthnicityType(StrEnum):
    WHITE = "Branca"
    BLACK = "Preta"
    BROWN = "Parda"
    INDIGENOUS = "Indígena"
    ASIAN = "Amarela"

class EducationType(StrEnum):
    NO_FORMAL_EDUCATION = "Não tenho Educação Formal"
    FUNDAMENTAL_INCOMPLETE = "Ensino Fundamental Incompleto"
    FUNDAMENTAL = "Ensino Fundamental Completo"
    MEDIUM_INCOMPLETE = "Ensino Médio Incompleto"
    MEDIUM = "Ensino Médio Completo"
    TECHNICAL = "Curso Técnico Completo"
    HIGHER_EDUCATION_INCOMPLETE = "Ensino Superior Incompleto"
    HIGHER_EDUCATION = "Ensino Superior Completo"
    POSTGRADUATION_INCOMPLETE = "Pós Graduação Incompleto"
    POSTGRADUATION = "Pós Graduação Completo"

class SocialLinkType(StrEnum):
    FACEBOOK = "Facebook"
    INSTAGRAM = "Instagram"
    TWITTER = "Twitter"
    TIKTOK = "TikTok"
    LINKEDIN = "LinkedIn"
    YOUTUBE = "YouTube"
    WEBSITE = "Website"

class DesabilityType(StrEnum):
    VISUAL = "Visual"
    HEARING = "Auditiva"
    PHYSICAL = "Física"
    INTELLECTUAL = "Intelectual"
    PSYCHOSOCIAL = "Psicossocial"
    MULTIPLE = "Múltipla"
    NONE = "Nenhuma"