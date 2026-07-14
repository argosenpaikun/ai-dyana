from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

resource = Resource.create(
    {
        "service.name": "ai-dyana",
        "service.version": "1.0.0",
        "deployment.environment": "development",
    }
)

provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

otl_exporter = OTLPSpanExporter(
    endpoint="http://otel-collector:4317",
    insecure=True
)

provider.add_span_processor(
    BatchSpanProcessor(otl_exporter)
)

def instrument(app):
    FastAPIInstrumentor.instrument_app(app)