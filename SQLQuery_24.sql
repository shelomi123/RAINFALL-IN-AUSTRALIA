SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
DROP TABLE [dbo].[Dim_WeatherConditions]
CREATE TABLE [dbo].[Dim_WeatherConditions](
	[ConditionID] [int] NOT NULL,
	[WindGustDir] [text] NULL,
	[WindDir9am] [varchar](10) NULL,
	[WindDir3pm] [varchar](10) NULL,
	[RainToday] [varchar](3) NULL,
	[RainTomorrow] [varchar](3) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Dim_WeatherConditions] ADD PRIMARY KEY CLUSTERED 
(
	[ConditionID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Dim_WeatherConditions]  WITH CHECK ADD CHECK  (([RainToday]='No' OR [RainToday]='Yes'))
GO
ALTER TABLE [dbo].[Dim_WeatherConditions]  WITH CHECK ADD CHECK  (([RainTomorrow]='No' OR [RainTomorrow]='Yes'))
GO
ALTER TABLE [dbo].[Dim_WeatherConditions]  WITH CHECK ADD CHECK  (([RainToday]='No' OR [RainToday]='Yes'))
GO
ALTER TABLE [dbo].[Dim_WeatherConditions]  WITH CHECK ADD CHECK  (([RainTomorrow]='No' OR [RainTomorrow]='Yes'))
GO
ALTER TABLE [dbo].[Dim_WeatherConditions]  WITH CHECK ADD CHECK  (([RainToday]='No' OR [RainToday]='Yes'))
GO
ALTER TABLE [dbo].[Dim_WeatherConditions]  WITH CHECK ADD CHECK  (([RainTomorrow]='No' OR [RainTomorrow]='Yes'))
GO
ALTER TABLE [dbo].[Dim_WeatherConditions]  WITH CHECK ADD CHECK  (([RainToday]='No' OR [RainToday]='Yes'))
GO
ALTER TABLE [dbo].[Dim_WeatherConditions]  WITH CHECK ADD CHECK  (([RainTomorrow]='No' OR [RainTomorrow]='Yes'))
GO
