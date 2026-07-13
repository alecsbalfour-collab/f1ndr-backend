from fastapi import APIRouter, HTTPException

from services.wchtr.renderer_service import RendererService
from models.wchtr.renderer_model import build_renderer_contract

# Import other engines' contracts
from services.scene.scene_service import SceneService
from services.animation.animation_timeline_service import AnimationTimelineService
from services.dialogue.dialogue_service import DialogueService
from services.wchtr.voice_service import VoiceService
from services.registry.registry_service import RegistryService

router = APIRouter()
renderer = RendererService()

scene = SceneService()
animation = AnimationTimelineService()
dialogue = DialogueService()
voice = VoiceService()
registry = RegistryService()

@router.post("/bind/all")
def bind_all():
    renderer.bind_scene(scene.snapshot())
    renderer.bind_animation(animation.snapshot())
    renderer.bind_dialogue(dialogue.history())
    renderer.bind_voice(voice.snapshot())
    renderer.bind_characters(registry.snapshot())

    return {"bound": True}

@router.get("/contract")
def get_renderer_contract():
    return build_renderer_contract(renderer.snapshot())
