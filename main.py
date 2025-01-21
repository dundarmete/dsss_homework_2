import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
from transformers import AutoModelForCausalLM, AutoTokenizer

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the LLM model and tokenizer
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Replace with your preferred model

logger.info("Loading the LLM model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to("cpu")
logger.info("Model loaded successfully!")

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_BOT_TOKEN = "7949393233:AAGlilskPan859lN6KIyyj5meHIA86SIUAQ"

# Function to handle the /start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I am your AI Assistant. Ask me anything!")

# Function to handle user messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    logger.info(f"Received message: {user_message}")
    
    # Generate response using the LLM
    inputs = tokenizer.encode(user_message, return_tensors="pt").to("cpu")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Send the response back to the user
    await update.message.reply_text(response)

# Function to handle errors
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Use filters.TEXT

    # Register the error handler
    application.add_error_handler(error)

    # Start the bot and let `run_polling()` handle initialization and shutdown
    application.run_polling()
