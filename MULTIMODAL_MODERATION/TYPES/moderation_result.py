from typing import ClassVar

from pydantic import BaseModel, Field, computed_field


class ModerationResult(BaseModel):

    rationale: str = Field(description="Explanation of what was harmful and why")
    flag_fields: ClassVar[tuple[str, ...]] = ()

    @computed_field  # type: ignore[misc]
    @property
    def is_flagged(self) -> bool:
        """Return True when any moderation flag is set."""
        return any(getattr(self, field, False) for field in self.flag_fields)


class TextModerationResult(ModerationResult):

    flag_fields: ClassVar[tuple[str, ...]] = ("contains_pii", "is_unfriendly", "is_unprofessional")
    contains_pii: bool = Field(description="Whether the message contains any personally-identifiable information (PII)")
    is_unfriendly: bool = Field(description="Whether unfriendly tone or content was detected")
    is_unprofessional: bool = Field(description="Whether unprofessional tone or content was detected")


class ImageModerationResult(ModerationResult):

    flag_fields: ClassVar[tuple[str, ...]] = ("contains_pii", "is_disturbing", "is_low_quality")
    contains_pii: bool = Field(
        description="Whether the image contains any person, part of a person, or personally-identifiable information (PII)"
    )
    is_disturbing: bool = Field(description="Whether the image is disturbing")
    is_low_quality: bool = Field(description="Whether the image is low quality")


class VideoModerationResult(ModerationResult):

    flag_fields: ClassVar[tuple[str, ...]] = ("contains_pii", "is_disturbing", "is_low_quality")
    contains_pii: bool = Field(
        description="Whether the video contains any person or personally-identifiable information (PII)"
    )
    is_disturbing: bool = Field(description="Whether the video is disturbing")
    is_low_quality: bool = Field(description="Whether the video is low quality")


class AudioModerationResult(ModerationResult):

    flag_fields: ClassVar[tuple[str, ...]] = ("contains_pii", "is_unfriendly", "is_unprofessional")
    transcription: str = Field(description="Transcription of the audio")
    contains_pii: bool = Field(
        description="Whether the audio contains any personally-identifiable information (PII) such as names, addresses, phone numbers"
    )
    is_unfriendly: bool = Field(description="Whether unfriendly tone or content was detected")
    is_unprofessional: bool = Field(description="Whether unprofessional tone or content was detected")
