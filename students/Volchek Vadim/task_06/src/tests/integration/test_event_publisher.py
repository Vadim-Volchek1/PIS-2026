"""
Integration-style test for RabbitMQ publisher.
"""
from unittest.mock import Mock, patch

from infrastructure.adapter.out.event_publisher_impl import EventPublisherImpl


class TestEventPublisher:
    @patch("infrastructure.adapter.out.event_publisher_impl.pika.BlockingConnection")
    @patch("infrastructure.adapter.out.event_publisher_impl.pika.URLParameters")
    def test_should_publish_bug_event(self, url_params_mock, connection_mock):
        fake_connection = Mock()
        fake_channel = Mock()
        fake_connection.channel.return_value = fake_channel
        connection_mock.return_value = fake_connection

        publisher = EventPublisherImpl("amqp://guest:guest@localhost:5672/")
        publisher.publish({"event_type": "BugCreated", "request_id": "BUG-2026-0001"})

        url_params_mock.assert_called_once()
        connection_mock.assert_called_once()
        fake_channel.queue_declare.assert_called_once_with(queue="bug_events", durable=True)
        fake_channel.basic_publish.assert_called_once()
        fake_connection.close.assert_called_once()
