{{config(materialized = 'table')}}

with raw_messages as (
    select
        id,
        sender,
        timestamp::timestamp as message_time,  -- Convert timestamp to timestamp type
        text,
        image,
        document
    from {{ source('data_hub','cleaned_data_table') }}  -- Reference the raw data source
)

-- Remove messages with no text, image, or document, and remove duplicates
select
    id,
    sender,
    message_time,
    text,
    image,
    document
from raw_messages
where text is not null
   or image is not null
   or document is not null
group by id, sender, message_time, text, image,document