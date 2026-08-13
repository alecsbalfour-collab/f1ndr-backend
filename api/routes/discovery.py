from fastapi import APIRouter, HTTPException

# Existing discovery engines
from discovery.scan import ScanEngine
from discovery.classify import DiscoveryClassifier
from discovery.generator import DiscoveryGenerator

router = APIRouter()

scan_engine = ScanEngine()
classifier = DiscoveryClassifier()
generator = DiscoveryGenerator()


@router.post("/discovery/scan")
def discovery_scan(payload: dict):
    """
    Run a discovery scan using the existing ScanEngine.
    """

    try:
        result = scan_engine.scan(payload)

        return {
            "status": "success",
            "engine": "discovery_scan",
            "input": payload,
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/discovery/classify")
def discovery_classify(payload: dict):
    """
    Classify discovery input using the existing DiscoveryClassifier.
    """

    try:
        result = classifier.classify(payload)

        return {
            "status": "success",
            "engine": "discovery_classify",
            "input": payload,
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/discovery/generate")
def discovery_generate(payload: dict):
    """
    Generate discovery feed items using the existing DiscoveryGenerator.
    """

    try:
        result = generator.generate(payload)

        return {
            "status": "success",
            "engine": "discovery_generate",
            "input": payload,
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
